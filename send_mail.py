# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.126.com'
EMAIL_HOST_USER = 'aoshanshouhuazhan@126.com'
# EMAIL_HOST_PASSWORD = 'HQOWWUWXKTINUCGY'
EMAIL_HOST_PASSWORD = 'bigticket@29'
EMAIL_PORT = 25

smtpserver = 'smtp.126.com'
user = 'aoshanshouhuazhan@126.com'
password = 'HQOWWUWXKTINUCGY'

sender = user
receiver = 'kgarnett29@126.com'
subject = '鳌山收花站'
msg = MIMEText('调用接口错误,正则匹配成功，但未找到对应的静态数据项','plain','utf-8')
msg['Subject'] = Header(subject, 'utf-8')

msg['from'] = 'aoshanshouhuazhan@126.com'
msg['to'] = 'kgarnett29@126.com'

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password) 
# smtp.sendmail(sender, receiver, msg.as_string())
smtp.sendmail(msg['from'], msg['to'], msg.as_string())

smtp.quit()
