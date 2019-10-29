#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/28 17:19
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : email_server_usage.py
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
import asyncore
import smtpd


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('来自：', peer)
        print('发送地址：', mailfrom)
        print('接收地址：', rcpttos)
        print('邮件长度：', len(data))


# server = CustomSMTPServer(('127.0.0.1', 8025), None)

# debug 模式
server = smtpd.DebuggingServer(('127.0.0.1', 8025), None)
asyncore.loop()
