#coding:utf-8

"""
    action:发送邮件
"""

import smtplib
from email.mime.text import MIMEText

class   SendEmail():
    def __init__(self):
        self.msg_from = '1196987863@qq.com'  # 发送方邮箱
        self.passwd = 'svuqvthbpgzgifji'  # 填入发送方邮箱的授权码

    def email(self):
        msg_to = 'penglei@bit-z.com'  # 收件人邮箱
        subject = "邮件测试"  # 主题
        # content = "测试邮件"    # 正文
        #HTML格式
        mail_msg = """           
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.runoob.com">这是一个链接</a></p>
        """
        msg = MIMEText(mail_msg,'html','utf-8')
        msg['Subject'] = subject
        msg['From'] = self.msg_from
        msg['To'] = msg_to
        try:
            server = smtplib.SMTP_SSL("smtp.qq.com", 465) # 邮件服务器及端口号
            server.login(self.msg_from, self.passwd)
            server.sendmail(self.msg_from, msg_to, msg.as_string())
            print "发送成功"
        except  Exception:
            print "发送失败"
        finally:
            server.quit()
