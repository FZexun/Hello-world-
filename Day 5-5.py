#!/usr/bin/python
# _ * _ coding: utf-8 _ * _

a = 20
b = 10
c = 15
d = 5
e = 0

e =(a + b) * c / d        #(30*15)/5
print('(a + b) * c / d运算结果为：', e)

e = ((a + b) * c) / d     #(30*15)/5
print('((a + b) * c / d运算结果为：', e)

e = (a + b) * (c / d)     #(30)*(15/5)
print('(a + b) * (c / d)运算结果为：', e)

e = a + (b * c) / d       #20+(150/5)
print('a + (b * c) / d运算结果为：', e)
