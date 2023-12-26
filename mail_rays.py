'''import smtplib
import ssl
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "suroliarahul9694@gmail.com"
password = input("Enter a password here: ")
reciever_email = "shivamnamedev14346@gmail.com"
message = """import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

text="Hi how are you"
html="<html><body><h1>Hi,how are you</h1></body></html>"

msg=MIMEMultipart()
msg['From']="suroliarahul9694@gmail.com"
msg['To']="singhjitesh575@gmail.com"
msg['subject']="html mail"
msg.attach(MIMEText(text,'plain'))
msg.attach(MIMEText(html,'html'))
filename="example.txt"
with open(filename,"rb") as attachment:
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment;filename=%s"%filename)
    msg.attach(p)

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(msg['From'],'lfcv ydaw oycu yzer')
s.sendmail(msg['From'],msg['to'],msg.as_string())
print("message sent successfully")
s.quit()
"""
smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp.login(sender_email, password)
smtp.sendmail(sender_email, reciever_email, message)
print("email send successfull")'''


# lfcv ydaw oycu yzer

# html content in email

'''import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

text="Hi how are you"
html="<html><body><h1>Hi,how are you</h1></body></html>"

msg=MIMEMultipart()
msg['From']="suroliarahul9694@gmail.com"
msg['To']="singhjitesh575@gmail.com"
msg['subject']="html mail"
msg.attach(MIMEText(text,'plain'))
msg.attach(MIMEText(html,'html'))
filename="example.txt"
with open(filename,"rb") as attachment:
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment;filename=%s"%filename)
    msg.attach(p)

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(msg['From'],'lfcv ydaw oycu yzer')
s.sendmail(msg['From'],msg['to'],msg.as_string())
print("message sent successfully")
s.quit()
'''



