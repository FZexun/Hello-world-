#!/usr/bin/python
# _*_ coding: utf-8 _*_

for num in range(10,20):         #迭代10到20之间的数字
    for i in range(2,num):       #根据因子迭代
        if num%i == 0:           #确定第一个因子
            j = num/i            #计算第二个因子
            print('%d 等于 %d * %d' % (num,i,j))
            break                #跳出当前循环
    else:                        #循环的else部分
        print(num,'是一个质数')
