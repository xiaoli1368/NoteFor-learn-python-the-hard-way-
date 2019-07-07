print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4) # 注意这里先算乘法后算求余
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) # 注意这里1/4结果为0.25，而2.0版本中1/4=0
print("Is it ture that 3 + 2 < 5 -7?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 >- 2)
print("Is it greater or equal?", 5 <= 2)
print("Is it less or equal?", 5 <= -2)

# 加分析题
# 1.给每一行进行注释
# 2.利用命令行的方式运行每一行，把Python当做计算器玩儿玩儿
# 3.自己找一个想要计算的东西，利用.py文件计算出来
# 4.关于1/4的结果为0还是0.25的思考
# 5.利用浮点数重写一遍。（提示：20.0是一个浮点数）