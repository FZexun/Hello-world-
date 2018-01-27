#!/usr/bin/python
# _*_ coding: utf-8 _*_

#打印1-9三角形阵列

for i in range(1,11):
    for k in range(1,i):
        print(k,  end="")
        k += 1
    i += 1
    print("")
