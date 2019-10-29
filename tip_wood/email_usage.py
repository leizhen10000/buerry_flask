#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/28 17:03
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : email_usage.py
# @Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃  ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃      ┻  ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import email
import logging
import os
import smtplib
from email.mime.text import MIMEText
from logging.handlers import SMTPHandler


def mail_process():
    # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger('test')

    mail_handler = SMTPHandler(
        mailhost=('smtp.qq.com', 25),
        fromaddr=username,
        toaddrs=[username],
        subject='应用已经中断，这个一个悲伤的时刻...',
        credentials=(username, ''),
        secure=()
    )
    mail_handler.setLevel(logging.INFO)

    logger.addHandler(mail_handler)

    try:
        x = 1 / 0
    except Exception:
        logger.error('计算出错')


def send_data():
    msg = MIMEText('这是消息主体')

    msg['To'] = email.utils.formataddr(('接收方', username))
    msg['From'] = email.utils.formataddr(('发送方', username))
    msg['Subject'] = '一个简单的测试消息'

    server = smtplib.SMTP('smtp.qq.com', 25)
    server.login(os.environ.get('MAIL_USERNAME'), os.environ.get('MAIL_PASSWORD'))
    server.set_debuglevel(True)
    # server = smtplib.SMTP('localhost', 8025)

    try:
        server.sendmail(username, [username], msg.as_string())
    finally:
        server.quit()


def handler_using():
    print('server', os.environ.get('MAIL_SERVER'))
    server = os.environ.get('MAIL_SERVER')
    print('port', os.environ.get('MAIL_PORT'))
    port = os.environ.get('MAIL_PORT')
    print('username', os.environ.get('MAIL_USERNAME'))
    username = os.environ.get('MAIL_USERNAME')
    print('password', os.environ.get('MAIL_PASSWORD'))
    password = os.environ.get('MAIL_PASSWORD')

    mail_handler = SMTPHandler(
        mailhost=(server, port),
        fromaddr=username,
        toaddrs=[username],
        subject='buerry',
        credentials=(username, password),
        secure=()
    )
    mail_handler.setLevel(logging.ERROR)
    logger = logging.getLogger('test1')
    logger.addHandler(mail_handler)
    logger.error('这应该没错了 chage server username subject')


if __name__ == '__main__':
    username = os.environ.get('MAIL_USERNAME')
    send_data()
    # mail_process()
    # handler_using()
