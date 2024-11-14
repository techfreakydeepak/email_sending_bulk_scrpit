#impoet the necessary modules
import smtplib, ssl, csv
from email.message import EmailMessage

sender = 'deepaksoi1810@gmail.com' #add your sender email address
password = 'aulnotullaubfglh' #add your app password

subject = 'server notice' #add the subject #add the subject to your email
body_message = 'Cors server will undergoes to maintenance' #type the message you want to send

#connect to our outgoing mail SMTP server
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context)

server.login(sender, password)

#The formula we will use to send emails
with open("C:\\Users\\HP\\Desktop\\Mails\\email testing.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        server.send_message(em)
        print("The message sent")

server.close()
print("Done @Cors")