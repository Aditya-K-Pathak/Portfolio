# # # Inbuilt Libraries =============================
# # import os
# # from tkinter import *
# # from tkinter import messagebox as tmsg
# # from PIL import Image, ImageTk

# # # User defined Libraries =============================
# # import Real_Time_Object_Detection as RT_detection
# # import Image_Window as NewWin
# # import Voice_Assistance as Va
# # import speech


# # # Function Definition For Image Window File =============================
# # def find():
# #     root.destroy()
# #     NewWin.create()


# # # Function Definition For Voice Command File =============================
# # def listen():
# #     root.destroy()
# #     Va.listen()


# # # Function to respond on clicking info Button =============================
# # def show():
# #     try:
# #         speech.speak("Opening Information of Project")
# #         res = ""
# #         with open("About.txt") as abt:
# #             res += abt.read()
# #             speech.speak(res)
# #     except:
# #         tmsg.showerror("Network Connection Error", 
# #         "Please Check your Internet Connection...")
# #     os.system("ABOUT.pdf")


# # root = Tk()
# # # Main screen Adjustment =============================
# # root.title("Object Detection System")  # Title of main window
# # root.geometry("1104x615")  # Dimension of main windows
# # # Fixing dimension of main windows
# # root.minsize(1104, 615)
# # root.maxsize(1104, 615)

# # # Background Image for main window=============================
# # image = Image.open("Resources/bg.jpg")
# # pic = ImageTk.PhotoImage(image)
# # label = Label(image=pic)
# # label.place(x=0, y=0)

# # # Button for live or Real_Time_Object_Detection file=============================
# # B1 = Button(text=" Live Object Detection", 
# #     width=30, command=RT_detection.start_webcam)
# # B1.place(x=786, y=424)

# # # Button for Image_Window file=============================
# # B2 = Button(text="Image Based Object Detection",
# #     width=30, command=find)
# # B2.place(x=786, y=545)

# # # Button for Voice_Assistance file=============================
# # B3 = Button(text="   🎙️", font=("Helvetica", 20), command=listen)
# # B3.place(x=40, y=350)

# # # Info Button ==========================
# # info_button = Image.open("Resources/info.png")
# # info_button_ = ImageTk.PhotoImage(info_button)
# # Button(image = info_button_, command = show).place(x=1050, y=50)

# # # Welcome Note ==========================
# # try:
# #     speech.speak("Welcome to Voice Command based Object Detection System...")
# # except Exception as e:
# #     tmsg.showerror("Network Connection Error",
# #         f"Please Check your Internet Connection...\nDetail: {e}")
# #     root.destroy()

# # root.mainloop()


# # # Inbuilt Libraries ============================
# # import speech_recognition as sr
# # import pyttsx3 
# # import webbrowser

# # # User defined files ============================
# # import Real_Time_Object_Detection as RT_detection
# # import Image_Window as newin


# # def listen():
# #     # Initialize the recognizer ============================
# #     r = sr.Recognizer() 
    
# #     def SpeakText(command):
# #         # Function to convert text to speech ============================
        
# #         # Initialize the engine
# #         engine = pyttsx3.init()
# #         engine.say(command) 
# #         engine.runAndWait()
    
# #     # Welcome voice Note ============================
# #     SpeakText("Voice Assistance Activated Say a Sentence with no or deactivate to stop voice assistance")
    
# #     # Infinite loop to hear ============================
# #     while(1):    
        
# #         try:
# #             # try statement to hold exceptions ============================
            
# #             # use the microphone as source for input. ============================
# #             with sr.Microphone() as source2:
                
# #                 print("Speak")
# #                 #listens for the user's input 
# #                 audio2 = r.listen(source2)
# #                 SpeakText("Recognizing Your Words! Thank you") 
# #                 # Using ggogle to recognize audio
# #                 MyText = r.recognize_google(audio2)
# #                 MyText = MyText.lower()
# #                 print(MyText)
    
# #                 if "deactivate" in MyText or "no" in MyText or "turn off" in MyText:
# #                     # if condition to check if their is an order to
# #                     # stop voice assistance
# #                     SpeakText("Voice Assistance Deactivated")
# #                     return "deactivate"
# #                     break

# #                 # elif left activated
# #                 elif "realtime" in MyText or "live"in MyText or "webcam" in MyText:
# #                     # checks if realtime or live as keyword in voice
# #                     # if found redirects to Real_Time_object_Detection file
# #                     SpeakText("Voice Assistanct will running in background, Webcam will be active soon") #Confirms that program will be active
# #                     RT_detection.start_webcam() # Initialize the file
# #                 elif "image" in MyText or "picture" in MyText or "photo" in MyText:
# #                     SpeakText("Voice Assistanct will be running in background, Enter File Location in Given Box with format") #Confirms that program will be active
# #                     newin.create() # New window to get image location is created
# #                 # else Speaks command not recognized/ find on google
# #                 else:
# #                     # search_terms = ["hello"]
# #                     # for term in search_terms:
# #                     url = "https://www.google.com.tr/search?q={}".format(MyText)
# #                     webbrowser.open_new_tab(url)
# #                     SpeakText("Sorry, Couldn't recognize it as a command, As an assistant I have redirected you to your search result in google")

# #         except sr.RequestError as e:
# #             # holds exceptions
# #             # print("Could not request results; {0}".format(e))
# #             SpeakText("Could not request results; {0}".format(e))
            
# #         except sr.UnknownValueError:
# #             # holds exceptions
# #             # print("unknown error occured")
# #             SpeakText("Some Error Occured")


# # # Inbuilt Libraries ============================ 
# # import cv2
# # import numpy as np
# # import os
# # import time
# # from tkinter import messagebox as tmsg
# # import speech


# # #  Method for main ============================
# # def start_scan(file_path):
# #     # print(file_path)
# #     yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# #     classes = []
# #     objects = ""

# #     with open("coco.names", "r") as file:
# #         classes = [line.strip() for line in file.readlines()]
# #     layer_names = yolo.getLayerNames()
# #     output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

# #     colorRed = (0, 0, 255)
# #     colorGreen = (0, 255, 0)

# #     # #Loading Images ============================
# #     name = file_path
# #     img = cv2.imread(name)
# #     height, width, channels = img.shape

# #     # # Detecting objects ============================
# #     blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# #     yolo.setInput(blob)
# #     outputs = yolo.forward(output_layers)

# #     class_ids = []
# #     confidences = []
# #     boxes = []
# #     for output in outputs:
# #         for detection in output:
# #             scores = detection[5:]
# #             class_id = np.argmax(scores)
# #             confidence = scores[class_id]
# #             # Checks probability of object
# #             if confidence > 0.5:
# #                 center_x = int(detection[0] * width)
# #                 center_y = int(detection[1] * height)
# #                 w = int(detection[2] * width)  # Width of box
# #                 h = int(detection[3] * height)  # Height of box

# #                 x = int(center_x - w / 2)  # X - Coordinate
# #                 y = int(center_y - h / 2)  # Y - Coordinate

# #                 boxes.append([x, y, w, h])  # Appends coordinates, length and width to boxes list
# #                 confidences.append(float(confidence))  # Appends possibility % to confidence list
# #                 class_ids.append(class_id)  # Appends name to class_ids list

# #     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
# #     for i in range(len(boxes)):
# #         if i in indexes:
# #             x, y, w, h = boxes[i]
# #             label = str(classes[class_ids[i]])
# #             objects += label + ", "
# #             cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)  # Generates and place a border
# #             cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 8, colorRed, 8)  # Generates and place name

# #     # cv2.imshow("Image", img)
# #     cv2.imwrite("output.jpg", img)  # Creates a new image file with frames and names
# #     tmsg.showinfo("Successful", "Your output image file is generated.\nKindly delete it after use")  # popup message
# #     speech.speak(f"{objects} detected")  # Speaks the names of detected Objects
# #     # print(objects)
# #     # time.sleep(1)  # Waits for 1 second to keep things in sync
# #     os.system("output.jpg")  # Display the image in default image viewing application

# #     # cv2.waitKey(0)
# #     cv2.destroyAllWindows()  # Destroys all window on completions


# # # Inbuilt Libraries =============================
# # from tkinter import *
# # from tkinter import messagebox as tmsg
# # from PIL import Image, ImageTk

# # # User defined Libraries =============================
# # import Image_Based_Object_Detection as IB_detection


# # def create():
# #     root1 = Tk()
# #     # Window's Detailing ============================= 
# #     root1.title("Image Based Object Detection")
# #     root1.geometry("1104x615")
# #     root1.minsize(1104, 615)
# #     root1.maxsize(1104, 615)

# #     # forward function invoked whenever "Find" Button is pressed
# #     def forward():
# #         path = e1.get()
# #         try:
# #             # try block to check if file is present
# #             IB_detection.start_scan(path)
# #         except:
# #             # shows file not found Error if no file is found
# #             tmsg.showerror("File Not Foud", f"No such file exist in path\n{path}")
# #         root1.destroy  # Destroys the window even if file is found or not

# #     # Adds Frame for easy updating =============================
# #     C1 = LabelFrame(root1, background="black", width=1104, height=615)
# #     C1.place(x=0, y=0)

# #     # Background Image =============================
# #     image = Image.open("Resources/object_background.jpg")
# #     pic = ImageTk.PhotoImage(image)
# #     Label(C1, image=pic).place(x=0, y=0)

# #     # Entry Box =============================
# #     e1 = StringVar()
# #     a = Entry(textvariable=e1, width=50)
# #     a.place(x=786, y=424)
# #     a.insert(0, "File Path")

# #     # Find Button to check for file =============================
# #     Button(C1, text="Find", command=forward).place(x=900, y=444)

# #     root1.mainloop()


# # # imported Libraries=============================
# # import cv2
# # import numpy as np
# # import time

# # # User-defined Library===========================
# # import speech


# # # Function Definition============================
# # def start_webcam():
# #     yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# #     classes = []

# #     # Reads Object name from coco.names==============
# #     with open("coco.names", "r") as file:
# #         classes = [line.strip() for line in file.readlines()]
# #     layer_names = yolo.getLayerNames()
# #     output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

# #     colorRed = (0, 0, 255)
# #     colorGreen = (0, 255, 0)

# #     # Starts VideoCapture============================
# #     cap = cv2.VideoCapture(1)
# #     # cap = cv2.VideoCapture(0)
# #     font = cv2.FONT_HERSHEY_SIMPLEX
# #     starting_time = time.time()
# #     frame_id = 0

# #     obj_name = ""
# #     while True:
# #         # #Loading WebCam Video======================
# #         _, img = cap.read()
# #         frame_id += 1
# #         height, width, channels = img.shape

# #         # # Detecting objects========================
# #         blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# #         yolo.setInput(blob)
# #         outputs = yolo.forward(output_layers)

# #         class_ids = []
# #         confidences = []
# #         boxes = []
# #         for output in outputs:
# #             for detection in output:
# #                 scores = detection[5:]
# #                 class_id = np.argmax(scores)
# #                 confidence = scores[class_id]
# #                 # Checks probability of object
# #                 if confidence > 0.5:
# #                     center_x = int(detection[0] * width)
# #                     center_y = int(detection[1] * height)
# #                     w = int(detection[2] * width)  # width of border
# #                     h = int(detection[3] * height)  # height of border

# #                     x = int(center_x - w / 2)  # x-coordinate
# #                     y = int(center_y - h / 2)  # y-coordinate

# #                     boxes.append([x, y, w, h])  # Appends coordinate, width and height to boxes list
# #                     confidences.append(float(confidence))  # Appends possibility % to confidence list
# #                     class_ids.append(class_id)  # Appends names to class_ids list
# #                     # obj_name += class_id + ", "

# #         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
# #         for i in range(len(boxes)):
# #             if i in indexes:
# #                 x, y, w, h = boxes[i]
# #                 label = str(classes[class_ids[i]])
# #                 obj_name += label + ", "
# #                 cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)  # Creates and place a border
# #                 cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 3, colorRed, 3)  # Creates and place name

# #         # Runs the Webcam
# #         cv2.imshow("Live Object Detection", img)

# #         # if object found==================================
# #         if obj_name != "":
# #             # Speaks object name===========================
# #             speech.speak(f"{obj_name} detected")
# #             # time.sleep(len(obj_name.split(", ")) + 2)
# #             # Empties object name==========================
# #             obj_name = ""
# #         else:
# #             speech.speak("No known object found")

# #         # Closes operation if 'q' button is pressed========
# #         if cv2.waitKey(1) == ord("q"):
# #             break


# # from gtts import gTTS
# # import time
# # import os


# # def speak(text):
# #         language = 'en'

# #         obj = gTTS(text=text, lang=language, slow=False)

# #         # Saving the converted audio in a mp3 file named
# #         # speech
# #         obj.save("speech.mp3")

# #         # Playing the converted file
# #         os.system("speech.mp3")
# #         time.sleep(2)


# from tkinter import *
# import tkinter.messagebox as msg

# root=Tk()
# def help():
#     a=msg.showinfo("Help","We are there to help you.")
#     print(a)

# root.title("Notes")
# mbar=Menu(root)
# m1=Menu(mbar)
# m1.add_command(label="Open file")
# # m1.add_command(label="Save as")
# # m1.add_separator()
# m1.add_command(label="Exit")
# root.config(menu=mbar)
# mbar.add_cascade(label="File",menu=m1)

# m2=Menu(mbar)
# m2.add_command(label="Help",command=help)
# root.config(menu=mbar)
# mbar.add_cascade(label="Help",menu=m2)

# e1=StringVar()
# a=Entry(textvariable=e1).pack(fill=X,)

# root.mainloop()


# s = ""
# at = [str(x) for x in input().split("\n")]
# print(at)

lst = ["call up",
"mobilize",
"stimulate",
"switch on",
"trigger",
"turn on",
"actuate",
"arouse",
"energize",
"impel",
"motivate",
"move",
"prompt",
"propel",
"rouse",
"start",
"stir",
"actify",
"set in motion",
"take out of mothballs"]

print(lst)