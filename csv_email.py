import smtplib
import csv
from email.message import EmailMessage


import getpass
password = getpass.getpass('비밀번호뭐니 : ')


f =open('pygj - email.csv', 'r', encoding= 'utf-8')


read_csv = csv.reader(f)
smtp_url = 'smtp.naver.com'
smtp_port = 465
s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('happylovetkd', password)

for line in read_csv:
    msg = EmailMessage()
    msg['Subject'] = "안녕하세요 안현상입니다"
    msg['From'] = "happylovetkd@naver.com"
    msg['To'] = line[1]
    msg.set_content(line[0] + '에게 보내는 메일입니다 오늘 점심은 양식으로 드시죠')
    s.send_message(msg)
    
f.close()
