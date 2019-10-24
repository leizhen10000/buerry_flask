#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/24 14:51
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : getattr_usage.py
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


class Student:
    name = "Albert"
    age = "20"

    def greet(self, message):
        print(message, self.name)


if __name__ == '__main__':
    student = Student()

    print(student.name)
    print(student.age)
    student.greet('hello')
    # 使用 getattr
    getattr(student, 'greet')('hello')
    # 使用 getattr 设置默认值
    print(getattr(student, 'description', 'no_des'))
