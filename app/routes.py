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
from flask import render_template, url_for, flash, redirect

from app import app

# view functions 视图函数
# 视图函数映射一个或多个 URL
from app.forms import LoginForm


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
    return render_template('index.html', title='主页', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me='
              f'{form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='登录', form=form)
