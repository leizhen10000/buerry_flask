#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/24 09:52
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : __init__.py.py
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
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

if app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_SERVER'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr=app.config['MAIL_USERNAME'],
            toaddrs=app.config['ADMINS'],
            subject='buerry',
            credentials=auth, secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # 设置文件日志 FileHandler
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_hadler = RotatingFileHandler('logs/buerry.log', maxBytes=20240,
                                      backupCount=10, encoding='utf-8')
    file_hadler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]'
    ))
    file_hadler.setLevel(logging.INFO)
    app.logger.addHandler(file_hadler)

    # 设置默认日志
    app.logger.setLevel(logging.INFO)
    app.logger.info('蓝莓网项目启动')

    # 测试发送邮件
    app.logger.error('问题出现了')

from app import routes, models, errors
