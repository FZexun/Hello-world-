#!/usr/bin/python
# _*_ coding: utf-8 _*_

#输出2到100间的质数
prime = []
for num in range(2,100):      #迭代2到100之间的数字
    for i in range(2,num):    #根据因子迭代
        if num%i == 0:        #确定第一个因子
           break              #跳出当前循环
    else:                     #循环的else部分
        prime.append(num)
print(prime)
    
