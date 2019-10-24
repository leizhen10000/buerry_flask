#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/10/24 10:34
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : all_usage_test.py
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
# 验证 name 在不同模块下的表现
from tip_wood import name_usage

print('=' * 30)

# 验证对 import 的限定
from tip_wood.import_usage import *

## 如果使用 from moudle import * ，那么通过 __all__ 可以限定
## 但是使用 form module import aps，特定的属性，不会有影响
spam()
from tip_wood.import_usage import aps as APS, blah

APS()
print(blah)
print('=' * 30)

## 如果 如下面这样导入，会导入 tip_wood.__init__.py 和 graphic.__init__.py 中的内容，再导入
## import 内容
## 但是：这里在第 27 行已经导入了 tip_wood 模块，所以不会在这显示 tip_wood.__init__.py中内容
from tip_wood.graphic import gen_graphic

print('=' * 30)
