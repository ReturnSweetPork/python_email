import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호뭐니 : ')

msg = EmailMessage()
msg['Subject'] = "제목은제목입니다!!!"
msg['From'] = "happylovetkd@naver.com"
msg['To'] = "2418486@hanmail.net"

msg.set_content('')
msg.add_alternative('''
<h1>안녕하세요!!</h1>
<p>저는 안현상입니다</p>
''', subtype="html")




smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('happylovetkd', password)
s.send_message(msg)
