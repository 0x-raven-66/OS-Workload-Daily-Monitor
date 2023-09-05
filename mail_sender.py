import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = ''
recv_email = ''

def setUpGmailSession():
    sender_pass = 'vftgshvtdhrnxeqm'
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()  # enable security
    session.login(sender_email, sender_pass)
    return session

def setUpEmailParts():
    # Email Header
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recv_email
    message['Subject'] = 'Semi Daily Workload Report'
    # The body and attachment file
    mail_text_body = "Hello, this is the semi daily report about your pc overall workload."
    message.attach(MIMEText(mail_text_body, 'plain'))
    attached_file_name = 'log_file.txt'
    # Open the file as binary mode
    attach_file = open(attached_file_name, 'rb')
    # for multipart email .... if you have an attachment so you specify its type then attach it to the email
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Disposition', 'attachment',filename=attached_file_name)
    # attache the payload that contain the attachment and its information
    message.attach(payload)
    # return the final email after setting all parts together
    return message.as_string()

def sendEmail():
        session = setUpGmailSession()
        final_message = setUpEmailParts()
        # send the mail
        session.sendmail(sender_email, recv_email, final_message)
        # destroy the session
        session.quit()
