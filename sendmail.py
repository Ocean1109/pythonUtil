import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def format_address(string):
    name, address = parseaddr(string)
    print(name,address)
    return formataddr((name, address))


if __name__ == '__main__':
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "15011099680@163.com"  # 用户名
    mail_pass = ""  # 授权密码

    sender = '15011099680@163.com'  # 发送方
    receivers = ['1667274497@qq.com']  # 接收方

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python发送邮件文本内容测试', 'plain', 'utf-8')
    message['From'] = format_address('Ocean<%s>' % sender)  # 发送者
    receivers_string = ''
    if len(receivers) == 1:
        receivers_string = format_address('收件人<%s>' % receivers[0])
    else:
        receivers_string = format_address('收件人<%s>' % receivers[0])
        for index in range(1, len(receivers)):
            receivers_string = receivers_string + ',' + format_address('收件人<%s>' % receivers[index])
    message['To'] = receivers_string  # 接收者
    message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
