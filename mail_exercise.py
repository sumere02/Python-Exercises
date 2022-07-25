import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

file = open("mails.txt","r",encoding="UTF-8")
mail_list = file.readlines()    
file.close()

message = MIMEMultipart()
message["From"] = "sumeremir70@gmail.com"
message["Subject"] = "Sending mail by using SMTP"
text = """
Corporate Mail With SMTP
Emir Sümer
"""
message_body = MIMEText(text,"plain")
message.attach(message_body)
for i in mail_list:
    message["To"] = i
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("sumeremir70@gmail.com","eXiled98")
        for i in mail_list:
            mail.sendmail(message["From"],message["To"],message.as_string())
    except:
        sys.stderr.write("Mail could not sent\n")
        sys.stdout.flush()