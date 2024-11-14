import csv
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Your SendGrid API key
SENDGRID_API_KEY = 'your_sendgrid_api_key'
sender_email = 'deepaksoi1810@gmail.com'
subject = 'Server Notice'
body_message = 'Cors server will undergo maintenance.'

# Load email addresses from the CSV file
with open("C:\\Users\\HP\\Desktop\\Mails\\email testing.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    count = 0  # Counter for emails

    for row in datareader:
        email_address = row[0]

        # Create a SendGrid Mail object
        message = Mail(
            from_email=sender_email,
            to_emails=email_address,
            subject=subject,
            plain_text_content=body_message
        )

        try:
            # Send email
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(f"Message sent to {email_address}: {response.status_code}")
            count += 1

            # Add a delay after every 100 emails
            if count % 100 == 0:
                print("Pausing for 1 second to avoid rate limits.")
                time.sleep(1)

        except Exception as e:
            print(f"Failed to send to {email_address}: {e}")
