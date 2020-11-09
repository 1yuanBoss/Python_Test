#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Cjx'


import math
import unittest
import os, time, random
import subprocess

from multiprocessing import Process
from multiprocessing import Pool
from datetime import datetime, timedelta, timezone
from operator import itemgetter
from enum import Enum
import json
from turtle import *
from email.mime.text import MIMEText

#from mydict import Dict

#迭代测试 杨辉三角
def triangles(max):
    n = 0
    results = [1]
    while n < max:
        yield results
        temp = results.copy()
        #temp = results
        results.append(1)
        t = 0
        l = len(results)
        while t < l:
            if t != 0 and t != l-1:
                results[t] = temp[t-1]+temp[t]
            t += 1
        n = n + 1
    return 'done'

 #for t in triangles(10):
 #   print(t)

#map测试 修改大小写
def normalize(name):
    return name.capitalize()

L1 = ['adam','LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#filter实验 回数
def is_palindrome(n):
    s1 = str(n)
    s2 = s1[::-1]
    return s1 == s2

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')    

#sorted实验 回数

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=by_name))
print(sorted(students, key=by_score))

def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

def is_odd(n):
    return n % 2 == 1

print(list(filter(lambda n: n%2==1, range(1, 20))))

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


#类练习
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

#获取对象信息
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print(dir('Student'))
print(len('Student'))

#类属性
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

#使用@property
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


#枚举类
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')       

#错误处理
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('ValueError!')

main()

#单元测试
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('err')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        if self.score >= 0:
            return 'C'
        

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

#文件读写
fpath = 'txt.txt'
with open(fpath, 'r') as f:
    s = f.read()
    print(s)

#内存读写
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


#操作文件目录
print(os.name)
print(os.path.abspath('.'))
#os.mkdir('/Users/michael/testdir')
dirl = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirl)

#dir -l
pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

#遍历所有文件查相应字符串文件
print('include txt file')

def find_file(file_dir, find):
    for root, dirs, files in os.walk(file_dir):
        for kk in files:
            if find in kk:
                print('find:', root+'\\'+kk)  # 当前目录路径

find_file('.', 'txt')

#datetime
'''
print('datetime 测试')

def to_timestamp(dt_str, tz_str):
    utc_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    ind1 = tz_str.find('C') + 1
    ind2 = tz_str.find(':') 
    ppp = tz_str[ind1:ind2]
    utc = int(ppp)
    dt = utc_dt.astimezone(timezone(timedelta(hours=utc)))
    print(utc_dt.timestamp())
    print(dt)
    return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
'''
#JSON
print('JSON 测试')
obj = dict(name='小明', age=20)
s = json.dumps(obj,ensure_ascii=False)
print(s)
'''
# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()
'''

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#多进程
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

#进程池
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

#文档测试
if __name__ == '__main__':
    unittest.main()

def fact(n):
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()



