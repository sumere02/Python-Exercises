import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()
message["From"] = "sumeremir70@gmail.com"
message["To"] = "sumeremir70@gmail.com"
message["Subject"] = "Sending mail by using Smtp"
text = """
Sending mail with SMTP

Emir Sümer
"""
message_body = MIMEText(text,"plain")
message.attach(message_body)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("sumeremir70@gmail.com","eXiled98")
    mail.sendmail(message["From"],message["To"],message.as_string())
    print("Mail Sent succesfully")
    mail.close()
except:
    sys.stderr.write("Mail could not sent")
    sys.flush()
    sys.exit()