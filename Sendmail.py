# -*- coding : utf-8 -*-
#@Time : 2020/01/07 14:33
#Auther :QIN
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time,os

class SendEmail:

    def send_mail(self):
        # 第三方 SMTP 服务
        mail_host = "smtp.163.com"  # 设置服务器
        mail_user = "amazing_qinlei@163.com"  # 用户名
        mail_pass = "QWERTY1234"  # 口令,QQ里面的授权码
        receivers = ['373912677@qq.com', 'amazing_qinlei@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        msg = MIMEMultipart()  # 创建一个带附件的实例
        msg["Subject"] = "测试报告，详情请见附件"
        msg["From"] = mail_user
        msg["To"] = ','.join(receivers)

        # ---文字部分---
        part = MIMEText("阿肥请查收，谢谢！")
        msg.attach(part)

        # ---附件部分---
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        #filename = "/Users/dev/Documents/interface_demo01/report/" + now + '-report.html'
        filename = os.getcwd() + '/report/' + '用例报告' + now + ".html"

        part = MIMEApplication(open(filename, 'rb').read(), encoding="utf-8")
        print(filename)
        part.add_header('Content-Disposition', 'attachment', filename="Result.html")
        msg.attach(part)

        try:
            s = smtplib.SMTP("smtp.163.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
            s.login(mail_user, mail_pass)  # 登陆服务器
            s.sendmail(mail_user, receivers, msg.as_string())  # 发送邮件
            s.close()
        except Exception as e:
            print("error:", e)



