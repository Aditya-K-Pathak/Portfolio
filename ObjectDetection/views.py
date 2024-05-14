from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
import cv2
from .import forms
import numpy as np
import datetime
import FullStack.mailverification as mail

URL = 'aditya2874.pythonanywhere.com/surveillance'

def get_mail(username: str, objects: any) -> str:
    ALERT = '''
<!DOCTYPE html>
<html>
<head>
<title>Security Alert - Suspicious Activity Detected</title>
<style>
  body {
    font-family: Arial, sans-serif;
    font-size: 16px;
    margin: 0;
    padding: 0;
  }
  h2 {
    color: #333;
    font-size: 20px;
    margin-bottom: 10px;
  }
  p {
    margin: 0 0 15px;
  }
  a {
    color: #333;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  .important {
    font-weight: bold;
  }
  .reference {
    margin-top: 20px;
    border-top: 1px solid #ddd;
    padding-top: 10px;
  }
  .reference dt {
    display: inline-block;
    width: 120px;
    text-align: left;
  }
  .reference dd {
    margin-left: 120px;
  }
</style>
</head>
<body>
  <h2>Alert! Suspicious Activity Detected</h2>
  <p>Dear [Recipient Name],</p>
  <p>Our security system detected potential suspicious activity at your property at [Time of Detection]. The camera identified a/an [Object Detected].</p>
  <p class="important">We recommend logging into your security dashboard at <a href="[Login URL]">[Login URL]</a> to view the live video feed and assess the situation.</p>
  <div class="reference">
    <dl>
      <dt>Object Detected:</dt>
      <dd>[Object Detected]</dd>
      <dt>Time of Detection:</dt>
      <dd>[Time of Detection]</dd>
    </dl>
  </div>
  <p>If you believe this is a genuine security threat, please contact phone:112 immediately.</p>
  <p>**Please note:** This is an automated email notification.</p>
  <p>Sincerely,</p>
  <p>AI Security System</p>
</body>
</html>
'''

    ALERT = ALERT.replace('[Recipient Name]', username)
    ALERT = ALERT.replace('[Time of Detection]', str(datetime.datetime.now()))
    ALERT = ALERT.replace('[Object Detected]', str(objects))
    ALERT = ALERT.replace('[Login URL]', URL)
    return ALERT

def index(request):
    return render(request, 'video.html', {'form': forms.ObjectForm})

def video_feed(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        objects = request.POST.get('objects').split(',')
        objects = set([object.strip().lower() for object in objects])
    # Open the video capture device
    try:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    except:
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    yolo = cv2.dnn.readNet("ObjectDetection/yolov3.weights", "ObjectDetection/yolov3.cfg")
    classes = []

    # Reads Object name from coco.names==============
    with open("ObjectDetection/coco.names", "r") as file:
        classes = [line.strip() for line in file.readlines()]
    layer_names = yolo.getLayerNames()
    output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

    colorRed = (0, 0, 255)
    colorGreen = (0, 255, 0)

    def generate_frames():
        while True:
            # Capture frame-by-frame
            ret, img = cap.read()
            if not ret:
                break
            height, width, channels = img.shape

            # # Detecting objects========================
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

            yolo.setInput(blob)
            outputs = yolo.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    # Checks probability of object
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)  # width of border
                        h = int(detection[3] * height)  # height of border

                        x = int(center_x - w / 2)  # x-coordinate
                        y = int(center_y - h / 2)  # y-coordinate

                        boxes.append([x, y, w, h])  # Appends coordinate, width and height to boxes list
                        confidences.append(float(confidence))  # Appends possibility % to confidence list
                        class_ids.append(class_id)  # Appends names to class_ids list
                        # obj_name += class_id + ", "

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    if label in objects:
                        mail.Mail().sendMail(
                            subject = 'Surveillance Alert - Aditya Pathak',
                            receiverAddress = email,
                            mail = get_mail(username, objects) 
                            )
                        return HttpResponse(request, '<h1>We have observed some suspicious activity</h1>')
                    # obj_name += label + ", "
                    cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)  # Creates and place a border
                    cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 3, colorRed, 3)  # Creates and place name

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', img)
        frame_data = buffer.tobytes()

        # Yield the frame data as a multipart/x-mixed-replace stream
        yield (b'--img\r\n'
                b'Content-Type: image/jpg\r\n\r\n' + frame_data + b'\r\n')

    # Video streaming using StreamingHttpResponse
    response = StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame")
    return response

# a = get_mail('sdjshj', 'shdsdhksa')
# print(a)