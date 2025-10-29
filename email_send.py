
#import libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

msg=MIMEMultipart()

#address of sender and reveiver

msg.add_header("From", sender)
msg.add_header("To", recipient1)
msg.add_header("To", recipient2)

#For copying and “blind copying” additional recipients, use the following statements:
msg.add_header("Cc", recipient3)
msg.add_header("Bcc", recipient4)

#subjectLine
msg.add_headr("Subject", subjectLine)

#Message
msg.attach(MIMEText(body, "plain"))
#You can also attach an HTML version by calling
msg.attach(MIMEText(htmlBody, "html"))

#attach Image
file=open("myimage.jpg" "rb")
img=MIMEImage(file.read())
file.close()
msg.attach(img)

#attach PDF or file
fp=open("/somedir/myile.pdf", "rb")
attachment = MIMEApplication(fp.read())
fp.close()
attachment.add_header("Content-Disposition","attachment; filename=myfile.pdf")
msg.attach(attachment)

#____________________________________
#sending message

import smtplib

host="smtp.gamil.com"
port=587
server=smtplib.SMTP(host,port)

server.starttls()

#login
server.login(username,password)
server.send_message(msg)
server.quit()

