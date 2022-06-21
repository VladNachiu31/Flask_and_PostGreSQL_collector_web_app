import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email, height, average_height, count):
    from_email = " Email Address "
    from_password = " Password "
    to_email = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>%s<strong>. Average height of all is <strong>%s<strong> and that is calculated out <strong>%s<strong> of people." % (
        height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    # Gmail log in
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.echlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
