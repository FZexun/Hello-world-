#!/usr/bin/python
# _*_ coding: utf-8 _*_

#打印菱形
rows = int(input('输入列数：'))
i = j = k = 1
print('打印空心等菱形，这里去掉if-else条件判断就是实心的')
for i in range(rows):   #变量i控制行数
    for j in range(rows - i): #(1,rows-i)
        print(' ',end=' ')
        j += 1
    for k in range(2 * i - 1): #(1,2*i)
        if k == 0 or k == 2 * i - 2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        k += 1
    print('\n')
    i += 1
    #菱形的下半部分
for i in range(rows):
    for j in range(i):  #(1,rows-i)
        print(' ',end=' ')
        j += 1
    for k in range(2*(rows - i) - 1):    #(1,2*i)
        if k == 0 or k == 2 * (rows - i) - 2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        k += 1
    print('\n')
    i += 1
