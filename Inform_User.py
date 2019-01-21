import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def send_mail(user,text):
    try:

        message = MIMEMultipart()
        message["From"] = "Daily Reminder"
        message["To"] = user
        message["Subject"] = "I Have Some News!"
        message_text = text
        message_content = MIMEText(message_text, "html")
        message.attach(message_content)
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("mail address", "password")
        mail.sendmail(message["From"], message["To"], message.as_string())
        mail.close()

    except:
        sys.stderr.write("Something unexpected happened!")
        sys.stderr.flush()
