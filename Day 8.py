#!/usr/bin/python
# _*_ coding: utf-8 _*_

#摇色子
import random
import sys
import time

result = []
while True:
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    print(result)
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += ""
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + " -> " + '小' + '\n')
        time.sleep( 1 )   #睡眠一秒
    else:
        sys.stdout.write(pointStr + '->' + '大' + '\n')
        time.sleep(1)    #睡眠一秒
    result = []

#如何终止？
