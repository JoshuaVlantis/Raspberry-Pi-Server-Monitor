import subprocess as sp
import os
import smtplib
import ssl
import time

acc = str("PLACE GMAIL HERE OF RECIEVER")


def read_creds():
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


def backonline():
    port = 465

    sender, password = read_creds()

    recieve = acc

    message = """\
    Subject: Raspberry Pi is online

    Raspberry Pi is back online

    """

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("sent email!")


def noserver():
    port = 465

    sender, password = read_creds()

    recieve = acc

    message = """\
    Subject: Raspberry Pi has no Connection to PME Server

    Connection to the PME server is down.

    """

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("sent email!")


def reboot():
    port = 465

    sender, password = read_creds()

    recieve = acc

    message = """\
    Subject: Raspberry Pi Rebooting

    Connection to the server is back rebooting raspberry pi

    """

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("sent email!")


i = 0
x = 0
time.sleep(5)
backonline()

while True:

    print(" ")
    time.sleep(5)
    ip = ""
    status, result = sp.getstatusoutput("ping -c1 -w2 " + ip)
    if status == 0:
        print("Server is UP")
        if i == 10:
            os.system('python reboot.py')
            print("Calling reboot of PI")
            reboot()
            time.sleep(10)
            os.system('sudo shutdown -r now')

        i = 0
    else:
        print("No Server found")
        if i < 2:

            print("Waiting for server to reconnect")

            i = i + 1
        else:
            if x == 0:
                noserver()
                x = 1
            print("Ready to reboot")
            i = 10
