import smtplib

from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.smtp_address = os.getenv("EMAIL_PROVIDER_ADDRESS")
        self.email = os.getenv("MY_EMAIL")
        self.email_pass = os.getenv("EMAIL_PASS")
        self.connection = None



    def send_email(self, email_list, email_body):
        self.connection = smtplib.SMTP(os.getenv("EMAIL_PROVIDER_ADDRESS"), port=587)
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_pass)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
