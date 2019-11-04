#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/4 13:29
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : email.py
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
from flask import current_app, render_template

from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[蓝莓网]重置密码',
               sender=current_app.config['ADMINS'][-1],
               recipients=[user.email],
               text_body=render_template(
                   'email/reset_password.txt', user=user, token=token),
               html_body=render_template(
                   'email/reset_password.html', user=user, token=token))
