width = int(input('输入对角线长度：'))
for row in range(width+1):
    for col in range(width+1):
        if ((abs(row-width/2)+abs(col-width/2))==width/2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(' ')
