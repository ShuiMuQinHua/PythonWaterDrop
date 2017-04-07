#coding=UTF8

import smtplib
from email.mime.text import MIMEText

SMTPserver = 'smtp.exmail.qq.com'
sender = 'hon******@rayjoy.com'
password = "x$$$$$$20623&S"

message = 'Python send msg to you 你好'
msg = MIMEText(message, _subtype='plain', _charset='utf-8')

msg['Subject'] = 'Test Email by Python'
msg['From'] = sender
msg['To'] = '183*****375@qq.com'

mailserver = smtplib.SMTP(SMTPserver,  25)
mailserver.login(sender, password)
mailserver.sendmail(sender, [sender], msg.as_string())
mailserver.quit()
print ('send email success')