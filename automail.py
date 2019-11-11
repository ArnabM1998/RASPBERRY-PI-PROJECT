import RPi.GPIO as io
import smtplib
from time import sleep

io.setwarnings(False)
io.setmode(io.BOARD)
io.cleanup()
switch_Pin = 7
io.setup(switch_Pin, io.IN)

sender_email="Any email id"
password="sender_email id's password"
receiver_email="any email id"
subject = "New Message!!"
header = "To: " + receiver_email + "\n" + "From: " + sender_email + "\n" + "Subject: " + subject
body = "Switch is On and LED Blink."
message= header + "\n\n" + body

while True:
    print(io.input(switch_Pin))
    if(io.input(switch_Pin) == 1):
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(sender_email,password)
        s.sendmail(sender_email, receiver_email, message)
        s.quit()
        sleep(1)
    else :
        sleep(1)
