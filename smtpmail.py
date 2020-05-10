import os
import smtplib
from email.message import EmailMessage

#hidden email variables
EMAIL_ADDRESS = os.environ.get('SMTPEMAIL')
EMAIL_PASS = os.environ.get('SMTPPASS')

#client
email_recipient = 'tony.duchars@gmail.com'

#example of setting email type to send to client
confirmation = False
otp = True
forgot_password = False

if confirmation:
    with open('email_templates/confirmation.html', 'r', encoding='utf-8') as file:
        to_send = file.read()
        subject = 'Confirmation Email'
elif otp:
    with open('email_templates/otp.html', 'r', encoding='utf-8') as file:
        to_send = file.read()
        subject = 'OTP Email'
if forgot_password:
    with open('email_templates/forgot_password.html', 'r', encoding='utf-8') as file:
        to_send = file.read()
        subject = 'Forgot Password Email'

msg = EmailMessage()
msg['From'] = EMAIL_ADDRESS
msg['To'] = email_recipient
msg['Subject'] = subject
msg.set_content(to_send, subtype="html")

#due to using the SSL connection there is no need no for 
#extended hello func like ehlo() - now is secure from the start (port changes from ehlo 587 to ssl 465)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    smtp.send_message(msg)
    smtp.quit()
    print("MESSAGE SENT AND CLOSED CONNECTION")


#LOCAL DEBUG SMTP FOR THE DEVS

# with smtplib.SMTP('localhost', 1025) as smtp:
#     subject = 'subject'
#     body = 'body'

#     #format email without any need for modules
#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(EMAIL_ADDRESS, 'tony.duchars@gmail.com', msg)
#     print("************")
#     print("DEBUG SENT")
#     print("************")


