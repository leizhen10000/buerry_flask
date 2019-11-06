#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/11/6 17:29
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : mixin_usage.py
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


class Mixin1:
    def ask(self):
        print("mixin 1")


class Mixin2:
    def ask(self):
        print("mixin 2")


class BaseClass(object):
    def ask(self):
        print('base')


class MyClass(Mixin2, Mixin1, BaseClass):
    pass


class Vehicle(object):
    """基础的交通方式"""

    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        route = calculate_route(from_=self.position, to=destination)


def calculate_route(from_, to):
    print(from_, to)
    return from_, to


class RadioUserMixin(object):
    def __init__(self):
        self.radio = None

    def play_song_on_station(self, station):
        self.radio = station
        print('play radio', self.radio)


class Car(Vehicle, RadioUserMixin):
    def travel(self, **kwargs):
        super().travel('hometown')


class Boat(Vehicle):
    pass


class Plane(Vehicle):
    pass


class LoggedMappingMixin:
    """为 日志 添加 get/set/delete 操作"""
    __slots__ = ()  # 混入类没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, item):
        print('Getting', str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print(f'Setting {key} = {value}')
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting', str(key))
        return super().__delitem__(key)


obj = MyClass()
obj.ask()
car = Car('iceland')
car.travel()
car.play_song_on_station('ga')


# __slots__ 限制属性

class Student:
    __slots__ = ('name', 'age', 'set_name')


class GraduateStudent(Student):
    pass


s = Student()
s.name = 'niu'
s.age = 12
# 如果添加其他属性，会抛出 AttributeError
try:
    s.score = 99
except AttributeError as e:
    print('错误的属性', e)


# 添加方法给实例
def set_name(self, name):
    self.name = name


from types import MethodType

s.set_name = MethodType(set_name, s)

s.set_name('new_niu')
print(s.name)

# 绑定方法到类中
Student.set_name = MethodType(set_name, Student)
s1 = Student()
s2 = Student()
s1.set_name('name1')
s2.set_name('name2')
print(s1.name, s2.name)


# 这里 s1,s2 都指向了相同的 set_name 所在的地址，所以 s2 把 s1 的值覆盖了

class Student1:
    pass


Student1.set_name = set_name
s1.set_name('name1')
s2.set_name('name2')
print(s1.name, s2.name)
# 同样的结果
