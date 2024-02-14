import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

VERIFICATIONMAILTEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Email Verification</title>
    <style>
      body {
        color: white;
        min-height: 100vh;
        background-color: black;
      }

      /* Header */

      header {
        display: flex;
        padding: 15px;
        justify-content: center;
        align-items: center;
        border-bottom: solid white 1px;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
      }

      header #logo {
        font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
          "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
      }
      body {
        font-family: Arial, sans-serif;
        background-color: #000000;
        margin: 0;
        padding: 0;
        color: #ffffff;
      }

      .container {
        width: 100%;
        max-width: 600px;
        margin: 20px auto;
        background-color: #1a1a1a;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      }

      .header {
        background-color: #333333;
        border-radius: 10px 10px 0 0;
        padding: 20px 0;
        text-align: center;
      }

      .header h2 {
        color: #ffffff;
        margin: 0;
      }

      .content {
        padding: 20px;
      }

      .content p {
        color: #ffffff;
        margin: 0 0 10px 0;
        line-height: 1.5;
      }

      .verification-pin {
        color: #3498db;
        font-size: 24px;
        font-weight: bold;
        margin-top: 0;
        text-align: center;
      }

      .footer {
        background-color: #333333;
        border-radius: 0 0 10px 10px;
        padding: 20px;
        text-align: center;
      }

      .footer p {
        color: #ffffff;
        margin: 0;
        line-height: 1.5;
      }

      .footer a {
        color: #3498db;
        text-decoration: none;
      }
    </style>
  </head>
  <body>
    <header>
      <span id="logo"> Aditya Pathak </span>
    </header>
    <div class="container">
      <div class="header">
        <h2>Email Verification</h2>
      </div>
      <div class="content">
        <p>Hello __username__,</p>
        <p>
          Thank you for signing up. To complete your registration, please use
          the following verification PIN:
        </p>
        <p class="verification-pin"> __verification_pin__</p>
        <p>Enter this PIN on the verification page to activate your account.</p>
        <p>
          If you did not request this verification, you can safely ignore this
          email.
        </p>
      </div>
      <div class="footer">
        <p>
          For assistance, please contact me at
          <a href="mailto:adityapathak2874@gmail.com">adityapathak2874@gmail.com</a>
        </p>
      </div>
    </div>
  </body>
</html>
"""

class Mail:
    def __init__(self):
        self.sender = 'weatherupdate.adityapathak@gmail.com'
        self.password = 'laxt lrmv jpxs fsng'

    def sendMail(self, receiverAddress: str, mail: str):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        message = MIMEMultipart()
        message['From'] = 'Aditya Pathak'
        message['To'] = receiverAddress
        message['Subject'] = 'HTML Email Test'
        message.attach(MIMEText(mail, 'html'))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(self.sender, self.password)
            server.send_message(message)

class validationHandler:
    @staticmethod
    def initiateValidation(Name: str, email: str) -> bool:
        with open('static/log/verification.log', 'a') as file:
            pin = {random.randint(100000, 999999)}
            file.write(f'{email}:{pin}')
            userTemplate = VERIFICATIONMAILTEMPLATE
            userTemplate = userTemplate.replace('__username__', Name)
            userTemplate = userTemplate.replace('__verification_pin__', str(pin))

        try: 
            Mail().sendMail(email, userTemplate)
            return True
        except:return False

    @staticmethod
    def checkValidation(email: str, pin: str) -> bool:
        with open('static/log/verification.log', 'r') as file:
            logs = file.readlines()
            for i in range(len(logs)):
                user_log = logs[i].split(':')
                if user_log[0] == email and user_log[1][1: -1] == pin:
                    return True
            return False
        