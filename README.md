# 📧 Email Automation System (Python)

The **Email Automation System** is a Python-based tool designed to send personalized emails to a list of recipients automatically.  
It uses a text template for the email body, a CSV file for recipient data, and Python’s SMTP library to deliver messages.  
Every email sent is also recorded in an Excel file, so you always have a full history of your communication.

This project is perfect for students, small businesses, newsletters, schools, and anyone who needs to send bulk emails efficiently.

---

## ⭐ Features

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

### 📌 What each file does

| File | Purpose |
|------|---------|
| `email_automation.py` | Reads template + CSV, sends emails, logs results |
| `config.py` | Stores email address, app password, SMTP server info |
| `recipients.csv` | Contains recipient names and email addresses |
| `welcome.txt` | The email body (with placeholders) |
| `email_log.xlsx` | Records all successful/failed emails |

---

## 🔧 Installation & Setup

### 1. Install Required Python Libraries

```bash
pip install pandas openpyxl
```

### 2. Set Up Email Credentials
