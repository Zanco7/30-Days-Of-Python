# Day 29 — Simple Email Sender

This project is a **Simple Email Sender** built using Python as part of my **30-Day Python Challenge**.

The app allows users to send emails directly from Python using **Gmail’s SMTP server**.

## Features
- Sends emails using Gmail SMTP
- Accepts sender, recipient, subject, and message body
- Uses secure SSL connection
- Displays success or error messages clearly

## How It Works
1. The user enters their email address.
2. The user provides a **Gmail App Password** (not the normal Gmail password).
3. The recipient email, subject, and message body are entered.
4. The program connects securely to Gmail’s SMTP server.
5. The email is sent successfully or an error message is shown.

## Requirements
- Python 3
- Internet connection
- Gmail account with **App Password enabled**

## How to Enable Gmail App Password
1. Enable **2-Step Verification** on your Google account.
2. Go to **Google Account → Security → App Passwords**.
3. Generate an app password for **Mail**.
4. Use that generated password in this program.

## How to Run

```bash
python simple_email_sender.py
```

## Concepts Used

* SMTP protocol
* Sending emails with Python
* Secure SSL connections
* Handling user input
* Error handling with try/except

## Author

Part of a 30-Day Python Challenge

