import key
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER = key.SENDER
PASSWORD = key.PASSWORD
VERIFICATIONMAILTEMPLATE = key.VERIFICATIONMAILTEMPLATE
RESPONSEMAILTEMPLATE = key.RESPONSEMAILTEMPLATE

class Mail:
    def __init__(self):
        self.sender = SENDER
        self.password = PASSWORD

    def sendMail(self, subject: str, receiverAddress: str, mail: str):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        message = MIMEMultipart()
        message['From'] = 'Aditya Pathak'
        message['To'] = receiverAddress
        message['Subject'] = subject
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
            file.write('\n')
            userTemplate = VERIFICATIONMAILTEMPLATE
            userTemplate = userTemplate.replace('__username__', Name)
            userTemplate = userTemplate.replace('__verification_pin__', str(pin))

        try: 
            Mail().sendMail('Mail Verification', email, userTemplate)
            return True
        except:return False

    @staticmethod
    def checkValidation(email: str, pin: str) -> bool:
        with open('static/log/verification.log', 'r') as file:
            logs = file.readlines()
            for i in range(len(logs)):
                user_log = logs[i].split(':')
                if user_log[0] == email and user_log[1][1: -2] == pin:
                    return True
            return False
        