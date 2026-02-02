import smtplib
from email.message import EmailMessage

# 30-day Python challenge
print("------30-day Python challenge 29/30------")
print("Simple Email Sender")

def send_email():
    sender_email = input("Enter your email: ").strip()
    app_password = input("Enter your app password: ").strip()  # Gmail requires app password
    recipient_email = input("Enter recipient email: ").strip()
    subject = input("Enter the subject: ").strip()
    body = input("Enter the message body: ").strip()

    # Create email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        # Connect to Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

send_email()
