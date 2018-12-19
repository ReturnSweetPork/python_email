import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호뭐니 : ')


email_list = ['happylovetkd@gmail.com', '2418486@hanmail.net']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "제목은제목입니다!!!"
    msg['From'] = "happylovetkd@naver.com"
    msg['To'] = email
    msg.set_content('내용은 내용입니다.!!!')
    
    

    smtp_url = 'smtp.naver.com'
    smtp_port = 465
    
    s = smtplib.SMTP_SSL(smtp_url, smtp_port)
    
    s.login('happylovetkd', password)
    s.send_message(msg)


