import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "luciusfremon@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "ckcraig2006@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=None) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

