#!/usr/bin/python
# _ * _ coding: utf-8 _ * _

# 例二：elif用法

num = 3
if num == 3:         #判断num的值
    print ('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:        #值小于零时输出
    print('error!')
else:
    print('roadman')
