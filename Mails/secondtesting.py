import smtplib, ssl, csv, time
from email.message import EmailMessage

# Sender's email details
sender = 'deepaksoi1810@gmail.com'
password = 'aulnotullaubfglh'

# Email subject and body
subject = 'Server Notice'
body_message = 'Cors(satellite station server all India) server will undergo maintenance .'

# Connect to the SMTP server
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
server.login(sender, password)

# Open the CSV file and send emails
with open("C:\\Users\\HP\\Desktop\\Mails\\email testing.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    count = 0  # Initialize email counter

    for row in datareader:
        # Create and configure the email message
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row[0]  # Assuming each row only contains an email address in the first column
        em['Subject'] = subject
        em.set_content(body_message)
        
        # Send the email and increment the counter
        server.send_message(em)
        print(f"Message sent to {row[0]}")
        count += 1

        # Pause after every 100 emails
        if count % 100 == 0:
            print("Pausing for 1 second to avoid rate limit.")
            time.sleep(1)

# Close the SMTP server connection
server.close()
print("Done @Cors(Deepaksingh)")



