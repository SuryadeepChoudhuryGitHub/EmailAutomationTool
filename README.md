# Email Automation System (Python)

The **Email Automation System** is a Python-based tool designed to send personalized emails to a list of recipients automatically.  
It uses a text template for the email body, a CSV file for recipient data, and Python’s SMTP library to deliver messages.  
Every email sent is also recorded in an Excel file, so you always have a full history of your communication.

This project is perfect for students, small businesses, newsletters, schools, and anyone who needs to send bulk emails efficiently.

---

## Features

- Send **bulk emails** automatically  
- Use **placeholders** like `{name}` for personalization  
- Read recipient details from a CSV file  
- Store email delivery logs in an Excel sheet  
- Fully configurable using a `config.py` file  
- Works with Gmail, Yahoo, Outlook, Zoho, and more  
- Simple, lightweight, and beginner-friendly project

---

## Project Structure

Suggested folder structure:

```text
email_automation/
email_automation.py     # main script (automation + logging)
config.py               # email and SMTP configuration
recipients.csv          # list of recipients
email_log.xlsx          # generated automatically (log of all emails)
templates/welcome.txt   # email body template
```

### What each file does

| File | Purpose |
|------|---------|
| `email_automation.py` | Reads template + CSV, sends emails, logs results |
| `config.py` | Stores email address, app password, SMTP server info |
| `recipients.csv` | Contains recipient names and email addresses |
| `welcome.txt` | The email body (with placeholders) |
| `email_log.xlsx` | Records all successful/failed emails |

---

## Installation & Setup

### 1. Install Required Python Libraries

```bash
pip install pandas openpyxl
```

### 2. Set Up Email Credentials
```text
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
```

### 3. Prepare
```text
name,email
Alice,alice@gmail.com
Bob,bob@yahoo.com
Charlie,charlie@hotmail.com
```

### 4. Create an Email Template
```text
Hello {name},
This is a test email from the Python automation script.
```

## Running the Program
```text
python main.py
```
### The program will:
- Load the template
- Read each receiver from recipients.csv
- Generate personalized emails
- Send them through SMTP
- Print “Sent to …” after each successful delivery
- Save a detailed history in email_log.xlsx

## How the system works
The Mail Automation system follows these steps:
### 1.Load template
  Reads the text file containing placeholders like {name}.
### 2.Load CSV recipients
  Reads details like name and email.
### 3.Personalize template
  Replaces all placeholders with actual data.
### 4.Send email
  Uses SMTP_SSL to deliver the email securely.
### 5.Log results
  Writes the timestamp, recipient info, and status to email_log.xlsx.

## Support Email Providers
| Provider        | SMTP Server         | Port |
| --------------- | ------------------- | ---- |
| Gmail           | smtp.gmail.com      | 465  |
| Yahoo           | smtp.mail.yahoo.com | 465  |
| Outlook/Hotmail | smtp.office365.com  | 587  |
| Zoho            | smtp.zoho.com       | 465  |

## Common Error and Fixes
### 1.Username and password not accepted
Solution:
- Use an App Password (not your normal Gmail password)
- Ensure 2-Step Verification is enabled

### 2. SMTP timed out
- Check your internet connection
- Check if your college/office WiFi blocks SMTP

Try using mobile hotspot

### 3. Placeholder errors
- Make sure template placeholders ({name}) match CSV column names exactly.

## Use Cases
- Sending event announcements
- College bulk updates
- Welcome or onboarding emails
- Newsletter distribution
- Marketing campaigns
- Customer communication

## Future Enhancements
  This project can be easily expanded with:
- HTML-based emails
- File attachments (PDF, certificates, invoices)
- GUI dashboard (Tkinter or web-based)
- Scheduling system for daily/weekly emails
- Multiple templates & campaigns
- Cloud deployment for full automation

## Acknowledgments
This project aims to help beginners understand:
- How email automation works
- How to use SMTP with Python
- How CSV + templates create personalized communication
- How logs can be stored in Excel for tracking
- Feel free to tweak and experiment with the project to make it your own!
