import smtplib, ssl


host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

username = "luciusfremon@gmail.com"
password = "thqdidpzbkxacvgb"

receiver = "ckcraig2006@gmail.com"

message = """\
Subject: Email from Portfolio App
Hi!
This is a new message.
"""

with smtplib.SMTP_SSL(host, port, context=None) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
