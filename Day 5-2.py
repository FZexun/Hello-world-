#!/usr/bin/python
# _ * _ coding: utf-8 _ * _

a = True
b = False

print('(a and b) = ',(a and b))
print('(a or b) = ',(a or b))
print('not(a and b) = ', not(a and b))

print('-----------------')

x = 10
y = 20

print ( '(x and y) = ',(x and y))
if (x and y):
    print('1-变量x和y都为true')
else:
    print('1-变量x和y有一个不为true')

print('(x or y) = ' , (x or y))
if( x or y):
    print('2-变量x和y都为true，或其中一个变量为true')
else:
    print('2-变量x和y都不为true')
    
#修改变量x的值
x = 0
print ( '(x and y) = ',(x and y))
if (x and y):
    print('3-变量x和y都为true')
else:
    print('3-变量x和y有一个不为true')

print('(x or y) = ' , (x or y))
if( x or y):
    print('4-变量x和y都为true，或其中一个变量为true')
else:
    print('4-变量x和y都不为true')

print('not(x and y) = ', not(x and y))
if not(x and y ):
    print('5-变量x和y都为false，或其中一个变量为false')
else:
    print('5-变量x和y都为true')



