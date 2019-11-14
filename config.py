#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/24 14:38
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : config.py
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
import os
import sys

base_dir = os.path.abspath(os.path.dirname(__file__))

WIN = sys.platform.startswith('win')
if WIN:  # win 系统使用三个斜杠
    prefix = 'sqlite:///'
else:  # 类 unix 系统使用四个斜杠
    prefix = 'sqlite:////'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ufuzbcyz_kiss_na'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              prefix + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮箱信息
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['leizhen8080@foxmail.com']
    # 分页相关配置
    POSTS_PER_PAGE = 4  # 显示的页面数


class TestConfig(Config):
    # 测试相关
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
