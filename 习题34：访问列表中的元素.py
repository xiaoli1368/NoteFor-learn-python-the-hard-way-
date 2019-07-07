# 这个是直接复制的

animals = ['bear','python','peacock','kangaroo','whale','platypus'] # 与 序号 相对应的每位选手的信息
#列出每行制定动物在animals列表中的基数
name_number = [1,2,0,3,4,2,5,4] # 序号，即 几号选手
ordinal = [2,3,1,4,5,3,6,5] # 每位选手的名次
for i in range(len(ordinal)):
    if ordinal[i] == 1:
        ordinal[i] = str(ordinal[i])+'st'
    elif ordinal[i] == 2:
        ordinal[i] = str(ordinal[i])+'nd'
    elif ordinal[i] == 3:
        ordinal[i] = str(ordinal[i])+'rd'
    else:
        ordinal[i] = str(ordinal[i])+'th'
i = 0
while i < 8:
    name = animals[name_number[i]]
    print ("The %s animal is at %d and is a %s" % (ordinal[i],name_number[i],name))
    i += 1
print('\nTurn Around: \n')    
i = 0
while i < 8:
    name = animals[name_number[i]]
    print ("The animal at %d is the %s animal and is a %s" % (name_number[i],ordinal[i],name))
    i += 1