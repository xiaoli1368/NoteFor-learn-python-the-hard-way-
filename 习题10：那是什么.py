# 关于转义字符
# \n 的换行
# \' 和 \" 对单引号和双引号的转义

print("I am 6'2\" tall.")
print('I am 6\'2" tall.')
# example1 = "I am 6\'2" tall." # 这个会报错，双引号不匹配
# 改成第二种方式可以匹配，因此单引号和双引号哪个在外边并不重要

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Python 中也允许使用 r'...' 表示内部字符串默认不转义
print('\\\n\\')
print(r'\\\n\\')

# 加分习题
# 1.搜索一下还有哪些可用的转义字符
# 2.使用三个单引号代替三个双引号，看看效果是不是一样的
# 3.将转义序列和格式化字符串放到一起，创建一种更复杂的格式
# 4.记得 %r 格式化字符串吗？使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。 
# 将 %r 和 %s 比较一下。 注意到了吗？%r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。