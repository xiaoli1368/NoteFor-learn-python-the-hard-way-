# 在本章的习题中主要使用复杂的字符串来建立一系列的变量
# 我们将键入大量的字符串、变量和格式化字符串，并且将他们打印出来。

x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those know %s." %(binary, do_not)
print(x)
print(y)
print("I said: %r." % x)
print("I also said: '%s'." % y)
# 注意这里的 %r 和 %s 
# repr() 函数处理对象与 str() 函数处理对象的差别。
# 详细分析可以见下面例子

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 
print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."
print(w+e)

# 加分习题
# 1.通读程序，注释每一行

# 2.找到所有的 “字符串包含字符长” 的位置，总共有四处

# 3.你确定只有四个位置吗？你怎么知道的？没准我在骗你呢

# 4.解释一下为什么 w 和 e 用 + 连起来就可以生成一个更长的字符串

'''一些常见的格式化输出符号
%s 字符串 (采用str()的显示)
%r 字符串 (采用repr()的显示)
%c 单个字符
%b 二进制整数
%d 十进制整数
%i 十进制整数
%o 八进制整数
%x 十六进制整数
%e 指数 (基底写为e)
%E 指数 (基底写为E)
%f 浮点数
%F 浮点数，与上相同
%g 指数(e)或浮点数 (根据显示长度)
%G 指数(E)或浮点数 (根据显示长度)
%% 字符"%"
'''

# 关于 %r 和 %s 的区别如下所示：
# \x27 就是单引号
print('%r'%'\x27') # 带括号的单引号
print('%s'%'\x27') # 纯单引号