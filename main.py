# email automation tool

import smtplib
from email.message import EmailMessage
import csv

from config import*


def get_template(temp_path: str):
    i = open(temp_path, "r")
    return str(i.read())


def get_recipients(csv_path: str):
    j = open(csv_path, "r")
    reader = csv.DictReader(j)
    for row in reader:
        yield row


def generate_Email(subject: str, body: str, to_email: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = EMAIL_ADDRESS
    message["To"] = to_email
    message.set_content(body)
    return message


def send_email(message: EmailMessage):
    with smtplib.SMTP_SSL(SERVER, PORT) as sm:
        sm.login(EMAIL_ADDRESS, PASSWORD)
        sm.send_message(message)


def send_all_emails(subject: str,
                    temp_path,
                    recipients_csv):
    template = get_template(temp_path)

    for reciever in get_recipients(recipients_csv):
        try:
            style = template.format(**reciever)

            message = generate_Email(
                subject=subject,
                body=style,
                to_email=reciever["email"],
            )
            send_email(message)
            print("Sent to", reciever['email'])

        except KeyError as f:
            print("Missing placeholder",{f},"for reciever:",{reciever})
        except Exception as f:
            print("Failed to send to",reciever.get('email'),f)



subject = "Test email!"
send_all_emails(subject, "templates/temp1.txt", "recipients.csv")
