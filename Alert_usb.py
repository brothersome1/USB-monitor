# alert_usb.py
import smtplib
from email.mime.text import MIMEText

def send_email(alerts):
    msg = MIMEText(alerts.to_string())
    msg['Subject'] = "USB Monitor Alert"
    msg['From'] = "monitor@example.com"
    msg['To'] = "securityteam@example.com"

    with smtplib.SMTP("smtp.yourmailserver.com", 587) as server:
        server.starttls()
        server.login("monitor@example.com", "yourpassword")
        server.send_message(msg)

# Example usage
# send_email(alerts)
