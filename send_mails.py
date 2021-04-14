from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import smtplib
from email.mime.base import MIMEBase
from email import encoders

def send_email(from_addr, to_addr_list, subject, plain_text_body,
              login, password, smtpserver='smtp.gmail.com:587',
              cc_addr_list=None, attachment=None, from_name=None):

    message=MIMEMultipart()

    plain=MIMEText(plain_text_body,'plain')

    message.add_header('from',from_name)
    message.add_header('to',','.join(to_addr_list))
    message.add_header('subject',subject)

    if attachment!=None:
        attach_file=MIMEBase('application',"octet-stream")
        attach_file.set_payload(open(attachment,"rb").read())
        encoders.encode_base64(attach_file)
        # f.close()
        # attach_file=MIMEApplication(open(attachment,"rb").read())
        attach_file.add_header('Content-Disposition','attachment', filename=attachment)
        message.attach(attach_file)


    message.attach(plain)

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr_list, message.as_string())
    server.quit()
    print("Sent to: ", to_addr_list)
