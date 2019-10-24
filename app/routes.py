#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/24 11:09
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : routes.py
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
from flask import render_template, url_for

from app import app


# view functions 视图函数
# 视图函数映射一个或多个 URL
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Buerry'}
    posts = [
        {
            'author': {'username': 'Arm'},
            'body': '我爱你中国'
        },
        {
            'author': {'username': 'Strong'},
            'body': '权力的游戏'
        }
    ]


    return render_template('index.html', title='Home', user=user, posts=posts)
