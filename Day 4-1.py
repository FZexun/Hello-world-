#!/usr/bin/python
# _ * _ coding :utf-8 _* _

a = 21
b = 10
c = 0

if ( a == b ):
    print('1-a等于b')
else:
    print('1-a不等于b')

if ( a !=b ):
    print('2 - a不等于b')
else:
    print('2 - a等于b')

if( a < b ):
    print('4 - a小于b')
else:
    print('4 - a大于等于b')

if( a > b ):
    print('5 - a大于b')
else:
    print('5 - a小于等于b')

#修改变量a和b的值
a = 5
b = 20
if(a <= b):
    print('6 - a小于等于b')
else:
    print('6 - a大于b')

if(b >= a):
    print('7 - b大于等于a')
else:
    print('7 - b小于a')
