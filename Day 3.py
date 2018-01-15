#!/usr/bin/python
#_*_ coding: utf-8 _*

list = [ 'runoob', 456 , 2.22, 'John' , 78.9 ]
tinylist = [123, 'john' ]

print(list)             #输出完整列表
print(list[0])          #输出列表的第一个元素
print(list[1:3])        #输出第二个至第三个元素
print(list[2:])         #输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)     #输出列表两次
print(list + tinylist)  #打印组合的列表

tuple = ( 'runoob' , 456, 2.22, 'john', 78.9)
tinytuple = (123, 'john')

print(tuple)                #输出完整元组
print(tuple[0])             #输出元组的第一个元素
print(tuple[1:3])           #输出第二个至第三个元素
print(tuple[2:])            #输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)        #输出元组两次
print(tuple + tinytuple)    #打印组合的元组

list[0] = 666
print(list[0])              #列表允许更新，元组不允许更新，元组中是非法应用
