import smtplib
from email.mime.text import MIMEText

from src.config import Config


class Mail:

    def __init__(self):
        self.config = Config()

        self.host = self.config.MAIL_SERVER
        self.port = self.config.MAIL_PORT
        self.username = self.config.MAIL_USERNAME
        self.password = self.config.MAIL_PASSWORD

    def connection(self):
        connection = None

        try:
            connection = smtplib.SMTP(host=self.host, port=self.port)
            connection.ehlo()
            connection.starttls()
            connection.login(self.username, self.password)
        except Exception as e:
            print(f"Error connecting to mail server, got {e}")

        return connection

    def sendmail(self, connection, subject: str, body: str, dest: str, sender: str):
        try:
            text_subtype = "plain"

            content = f"""\
                {body}
            """

            msg = MIMEText(content, text_subtype)
            msg["Subject"] = subject
            msg["From"] = sender

            connection.sendmail(msg=msg.as_string(), from_addr=sender, to_addrs=dest)
        except Exception as e:
            print(f"Error when sending email, got: {e}")
