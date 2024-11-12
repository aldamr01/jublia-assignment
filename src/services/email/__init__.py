import smtplib
from email.mime.text import MIMEText

class Mail:
    
    def __init__(self):
        self.host = "sandbox.smtp.mailtrap.io"
        self.port = 587
        self.username = "0b6b3b80de9def"
        self.password = "f2d25cc27b329e"
        
        self.connection = smtplib.SMTP(host=self.host, port=self.port)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.login(self.username, self.password)
        
    def sendmail(self, subject: str, body: str, dest: str, sender: str):
        try:
            cn = self.connection
            text_subtype = 'plain'

            content=f"""\
                {body}
            """
            
            msg = MIMEText(content, text_subtype)
            msg['Subject'] = subject
            msg['From'] = sender 

            cn.sendmail(msg=msg.as_string(),from_addr=sender, to_addrs=dest)
        except Exception as e:
            print(f"Error when sending email, got: {e}")