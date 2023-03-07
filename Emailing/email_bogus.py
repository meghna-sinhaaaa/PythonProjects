import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up email parameters
email_sender = "your_email@example.com"
email_password = "your_email_password"
email_subject = "Subject of your email"
email_body = "Body of your email"
recipient_list = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]

# Set up email message
message = MIMEMultipart()
message['From'] = email_sender
message['To'] = ", ".join(recipient_list)
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

# Send email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, email_password)
    text = message.as_string()
    server.sendmail(email_sender, recipient_list, text)
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print("Error sending email:", str(e))