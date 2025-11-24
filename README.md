# Email Automation Tool

This project is a simple email automation tool built in Python.  
It can:

- Send emails in bulk using SMTP (e.g., Gmail)
- Use a text template with placeholders like `{name}`
- Read recipients from a CSV file
- Log every sent/failed email into an Excel file (`email_log.xlsx`)

Basically, it’s a polite little robot that sends emails for you.

---

## Features

- **Bulk emailing**: Send the same email (with personalization) to multiple recipients.
- **Templating**: Use `{name}`, `{email}`, etc. in a text template.
- **CSV-based recipients**: Manage recipients easily using a spreadsheet-like CSV.
- **Excel logging**: Every email (sent or failed) is recorded in `email_log.xlsx`.
- **SMTP-based**: Works with Gmail or any other SMTP provider (with correct settings).

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
