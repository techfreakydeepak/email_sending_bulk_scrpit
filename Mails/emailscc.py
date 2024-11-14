import smtplib
from email.mime.text import MIMEText
import os

def send_email(sender_email, receiver_email, cc_emails, subject, body, reply_to_address):
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Cc'] = ', '.join(cc_emails)
    msg['Subject'] = subject
    msg['Reply-To'] = reply_to_address

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'deepaksoi1810@gmail.com'
    smtp_password = 'aulnotullaubfglh'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, [receiver_email] + cc_emails, msg.as_string())
            print('Email sent successfully!')
    except smtplib.SMTPAuthenticationError:
        print('Error: Authentication failed. Check your email address and password.')
    except Exception as e:
        print(f'Error in sending email: {e}')

if __name__ == '__main__':
    sender_email = 'deepaksoi1810@gmail.com'
    receiver_email = 'itsdeepaksingh00@gmail.com'
    cc_emails = ['goodwrite96@gmail.com','deepakcario173@gmail.com','soham.soi2024@gmail.com','kritianu0508@gmail.com','sneha2001@gmail.com','c_b_sng@yahoo.co.in']
    subject = 'Email Confirmation'
    body = 'Email Sent By Deepak, It is the confirmation that you have received the mail..'
    reply_to_address = 'itsdeepaksingh00@gmail.com'

    send_email(sender_email, receiver_email, cc_emails, subject, body, reply_to_address)