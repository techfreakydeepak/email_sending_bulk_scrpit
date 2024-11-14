import smtplib, ssl, csv, time
from email.message import EmailMessage
from email.mime.text import MIMEText
import os

# Sender email details
SENDER_EMAIL = 'deepaksoi1810@gmail.com'
PASSWORD = 'aulnotullaubfglh'

# Email subject and body
SUBJECT = 'Server Notice'
BODY_MESSAGE = 'Cors(satellite station server all India) server will undergo maintenance.'

# SMTP Server Details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT_SSL = 465
SMTP_PORT_TLS = 587

def send_email_with_cc(sender_email, receiver_email, cc_emails, subject, body, reply_to_address):
    """
    Sends an email with optional CC recipients.
    """
    msg = MIMEText(body)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Cc'] = ', '.join(cc_emails)
    msg['Subject'] = subject
    msg['Reply-To'] = reply_to_address
    
    try:
        # Connect to the SMTP server with TLS for added security
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT_TLS) as server:
            server.set_debuglevel(1)
            server.starttls(context=ssl.create_default_context())
            server.login(sender_email, PASSWORD)
            server.sendmail(sender_email, [receiver_email] + cc_emails, msg.as_string())
            print(f'Email successfully sent to {receiver_email} with CC: {cc_emails}')
    except smtplib.SMTPAuthenticationError:
        print('Error: Authentication failed. Check your email address and password.')
    except Exception as e:
        print(f'Error in sending email: {e}')

def batch_send_emails(csv_file_path):
    """
    Sends emails in batches of 100, pausing for 1 second after each batch.
    """
    count = 0  # Email counter
    
    # Open the CSV file and read email addresses
    with open(csv_file_path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        
        for row in datareader:
            # Prepare the email message
            receiver_email = row[0]  # Assuming each row has the email in the first column
            cc_emails = [
                'goodwrite96@gmail.com', 'deepakcario173@gmail.com',
                'soham.soi2024@gmail.com', 'kritianu0508@gmail.com',
                'sneha2001@gmail.com', 'c_b_sng@yahoo.co.in'
            ]
            reply_to_address = 'itsdeepaksingh00@gmail.com'

            # Send the email
            send_email_with_cc(SENDER_EMAIL, receiver_email, cc_emails, SUBJECT, BODY_MESSAGE, reply_to_address)
            count += 1

            # Pause every 100 emails to avoid rate limits
            if count % 100 == 0:
                print("Pausing for 1 second to avoid rate limit.")
                time.sleep(1)
    
    print("Done sending emails.")
