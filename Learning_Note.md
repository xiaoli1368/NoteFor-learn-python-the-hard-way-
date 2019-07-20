

# Learning Notes

作者：xiaoli1368
日期：2019/07/16
字数：17k




## 前言

> 这是《笨办法学Python 2.0》的学习笔记，主要是关于每一小节的技巧。加分习题部分没有直接展示出来，而是作为总结或者易错点直接在代码中注释了出来。
>



## 目录

[TOC]

## 习题0：准备工作

**主要内容：**

- Python环境的配置
- 当前我所使用的是Window环境，所需要的软件有：
  1. windown10 1809
  2. Python 3.6.4
  3. VsCode 1.36.1

**配置步骤简述如下：**

- 去[官网](https://www.python.org/)下载对应版本的Python并安装，配置环境变量，使用命令行验证是否成功安装
- 去[官网](https://code.visualstudio.com/)下载VsCode并安装，下载Python插件并配置
- 测试代码

**使用CMD运行python的结果如下：**

```python
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>python
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Ana
conda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**这里需要注意的一些技巧：**

- 使用命令行CMD以及PowerShell
- 熟悉命令行下的一些操作



## 习题1：第一个程序

**主要内容：**

- 使用print函数打印字符串

**代码如下：**

```python
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print("I 'd said do not touch this.")

# 一些常见的错误
# SyntaxError 语法错误

# 输出中文的一些测试
# --coding:utf-8--
print("你好，世界！")
# 果真中文的编码问题很大啊

# 加分习题
# 1.让你的脚本多打印一行，这是什么意思啊？
print("")

# 2.让你的脚本只打印一行
print("Hello World!", end="")
print("Hello Again", end="")
# 这里print前边有空格会报错，注意

# “#”号的作用就是注释
```

**结果如下：**

```python
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I 'd said do not touch this.
你好，世界！

Hello World!Hello Again
```

可以查看print函数的用法如下：

```python
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

通过查看使用说明，可以控制打印的字符串（数值），中间插入的字符，后面的两个变量用的不是特别多了。

**关键技巧：**

- print内部使用单引号或者双引号，应该是都可以的
- print内部可以使用三引号来打印段落

- 结尾不换行
- 打印含有转移字符的字符串
- 格式化输出
- 关于输出中文 # --coding:utf-8--



## 习题2：注释和井号

**主要内容：**

- 使用井号进行注释
- 使用三个单引号或者双引号进行注释
- 在VsCode中注释的快捷键是 ctrl+k c，取消注释的快捷键是 ctrl+k u

**代码如下：**

```python
# A comment,this is so you can read program later.
# Anything after the # is ignored by Python.

print("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print("This won't run")

print("This will run")

# 这里应该有一些拓展
# 如对于代码块应该如何进行注释:
# 三个单引号或者三个双引号

'''
asdfasfasg
'''

"""
sadfasdf
asfasf
"""
```

**结果如下：**

```python
I could have code like this.
This will run
```



## 习题3：数字和数字计算

**主要内容：**

- 处理数字和进行数学计算

**代码如下：**

```python
print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)          # 注意这里，结果是浮点数（区分 30/6 以及 30//6 ）
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

# 加分习题
# 1.给每一行进行注释
# 2.利用命令行的方式运行每一行，把Python当做计算器玩儿玩儿
# 3.自己找一个想要计算的东西，利用.py文件计算出来
# 4.关于1/4的结果为0还是0.25的思考
# 5.利用浮点数重写一遍。（提示：20.0是一个浮点数）
```

**结果如下：**

```python
I will now count my chickens:
Hens 30.0
Roosters 97
Now I will count the eggs:
6.75
Is it ture that 3 + 2 < 5 -7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? False
Is it less or equal? False
```

**注意：**

- 注意区分单除号和双除号的区别
- 双除号表示向下取整，精度保持一致
- 运算顺序



## 习题4：变量和命令

**主要内容：**

- 学习变量和命名

**代码如下：**

```python
cars = 100
sapce_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars- drivers
cars_driven = drivers
carpool_capacity = cars_driven * sapce_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# 加分习题
# 1.在程序中使用4.0作为space_in_a_car的值，这样做有必要吗？如果只用4会有什么问题
# 这里会影响到cars_not_driven的类型，4.0下是浮点数，输出为120.0
# 而4下是整数，输出为120

# 2.记住“4.0”是一个浮点数，自己研究一下这是什么意思。

# 3.在每一个变量赋值的上一行加上一行注释

# 4.记住 = 的名字是等于（equal），它的作用是为东西取名字

# 5.记住 _ 是下划线字符

# 6.将Python作为计算器运行起来，不过这一次在计算过程中使用变量名来做计算
# 常见的变量名有i,x,y等等
```

**注意技巧：**

- 变量命名，驼峰准则



## 习题5：更多的变量和打印

**主要内容：**

- 格式化字符串 format string

**代码如下：**

```python
my_name   = 'Zed A. Shaw'
my_age    = 35            # not a lie
my_height = 75            # inches
my_weight = 180           # lbs
my_eyes   = 'Blue'
my_teeth  = 'Whith'
my_hair   = 'Brown'

print("Let's talk about %s."  % my_name)
print("He's %d inches tall."  % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, and try to get it exactly right.
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# 加分习题
# 1.修改所有变量的名字，把他们前边的”my_“去掉。确认将每一个地方都去掉。

# 2.试着使用更多的格式化字符。例如 %r 就是一个非常有用的一个
# 它的含义是，不管什么都打印出来

# 3.在网上搜索所有的Python格式化字符

# 4.试着用变量将英寸和磅转换成厘米和千克。不要直接键入答案，
# 使用Python的计算功能来完成
```

**结果如下：**

```python
Let's talk about Zed A. Shaw.
He's 75 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually Whith depending on the coffee.
If I add 35, 75, and 180 I get 290.
```

**关键技巧：**

- 格式化字符串 format string

- 试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。



## 习题6：字符串和文本

**主要内容：**

- 在本章的习题中主要使用复杂的字符串来建立一系列的变量，键入大量的字符串、变量、和格式化字符，并且将它们打印出来。我们还将练习使用简写的变量名。

**代码如下：**

```python
x = "There are %d type of people." % 10
y = "Those who know %s and those know %s." %(binary, do_not)
binary = "binary"
do_not = "don't"
print(x)
print(y)
print("I said: %r." % x)         # 注意 %r 的外层没有引号
print("I also said: '%s'." % y)  # 注意 %s 的外层存在引号
# 注意这里的 %r 和 %s 的区别
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
print('%r' % '\x27') # 带引号的单引号
print('%s' % '\x27') # 纯单引号
```

**结果如下：**

```python
There are 10 type of people.
Those who know binary and those know don't.
I said: 'There are 10 type of people.'.
I also said: 'Those who know binary and those know don't.'.
Isn't that joke so funny?! False
This is the left side of ...a string with a right side.
"'"
'
```

**关键技巧：**

- %r 以及 %s 的区别
- 字符串之间使用+号进行拼接



## 习题7：更多打印

**主要内容：**

- 巩固你学到的东西，进行打印练习

**代码如下：**

```python
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow') # 思考一下这里改为 %r 则结果如何
print("And everyone thar Mary went.")
print("." * 10) # what'd that do # 666，居然直接打印了十个.

end1  = "C"
end2  = "h"
end3  = "e"
end4  = "e"
end5  = "s"
end6  = "e"
end7  = "B"
end8  = "u"
end9  = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end, try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 +end6,) # 好像在旧版本里，这里加逗号是为了不换行
print(end7 + end8 + end10 + end11 +end12)

# 说明：作者的版本可能会打印出这种效果：
print(end1 + end2 + end3 + end4 + end5 +end6, end7 + end8 + end10 + end11 +end12)

# 加分习题
# 接下来几节的加分习题是一样的
# 1.逆向阅读，在每一行上边加注释
# 2.倒着朗读出来，找出自己的错误
# 3.从现在开始，把你的错误记录下来，写到一张纸上。
# 4.在开始下一届习题时，阅读一遍你记录下来的错误，并且尽量避免在下个联系中再犯同样的错误
# 5.记住，每个人都会犯错误。程序员和魔术师一样，他们希望大家认为他们从不犯错，不过这只是
# 表象而已，他们每时每刻都在犯错
```

**结果如下：**

```python
Mary had a little lamb.
Its fleece was white as snow.
And everyone thar Mary went.
..........
Cheese
Buger
Cheese Buger
```

**关键技巧：**

- print函数使用“*”打印10个同样的内容



## 习题8：打印，打印

**主要内容：**

- 更多的关于格式化字符串输出的打印练习

**代码如下：**

```python
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)) # 注意用都逗号分隔，并且最后一处没有逗号

# 加分习题
# 1.自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯同样的错误
# 2.注意最后一行中既有单引号又有双引号，你觉得它是如何工作的？

# 为了区分 %r 和 %s 的区别，可以另外赋值
formatter = "%s %s %s %s"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
```

**结果如下：**

```python
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
1 2 3 4
one two three four
True False False True
%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s
I had this thing. That you could type up right. But it didn't sing. So I said goodnight.
```

**关键技巧：**

- 注意 %r 以及 %s 的区别



## 习题9：打印，打印，打印

**主要内容：**

- 更多的关于打印的练习

**代码如下：**

```python
days   = "Mon Tue Wes Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There 's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# 这里注意的有两点

# 1.转义字符 "\"
# "\n" 是 换行
# "\t" 是 tab
# "\\" 是 "\"

# 2.print 函数内部打印多行字符串用 """____"""

# 加分习题
# 1.自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯同样的错误
```

**结果如下：**

```python
Here are the days:  Mon Tue Wes Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There 's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
```

**关键技巧：**

- 关于转移字符的使用

- 2.print 函数内部打印多行字符串用 """____"""



## 习题10：那是什么？

**主要内容：**

- 转义字符的使用，\n 的换行，\' 和 \" 对单引号和双引号的转义

**代码如下：**

```python
print("I am 6'2\" tall.") # 其实只要首尾能够匹配上，中间直接转义就行
print('I am 6\'2" tall.')
# example1 = "I am 6\'2" tall." # 这个会报错，双引号不匹配
# 改成第二种方式可以匹配，因此单引号和双引号哪个在外边并不重要

tabby_cat     = "\tI'm tabbed in."
persian_cat   = "I'm split\non a line."
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
```

**结果如下：**

```python
I am 6'2" tall.
I am 6'2" tall.
	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass

\
\
\\\n\\
```

**关键技巧：**

- 转义字符
- \n 的换行，\' 和 \" 对单引号和双引号的转义



## 习题11：提问

**主要内容：**

- 关于input的使用

**代码如下：**

```python
print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh")
weight = input()
print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# 这里注意到输入光标在语句的下方，可以使用下种形式：
age    = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")
print("So, you're %s old, %s tall and %s heavy." % (age, height, weight))

# 加分习题
# 1.上网查询Python的raw_input实现的是什么功能？
# 2.你能找到它的别的用法吗？测试一下你上网搜到的例子。
# 3.用类似的格式再写一段，把问题改成你自己的问题。
# 4.和转义序列有关的，想想为什么最后一行 '6\2"' 里边有一个 \' 序列
# 单引号需要被转义，从而防止它被识别为字符串的结尾。有没有注意到这一点？

# 注意这里将第二组的输出改为了 %s ，注意与 %r 的区别
```

**结果如下：**

```python
How old are you?
 23
How tall are you?
 1.84
How much do you weigh
 74
So, you're '23' old, '1.84' tall and '74' heavy.
How old are you?  23
How tall are you?  1.84
How much do you weight?  74
So, you're 23 old, 1.84 tall and 74 heavy.
```

**关键技巧：**

- 使用input来读取输入的参数



## 习题12：提示别人

**主要内容：**关于input的使用

**代码如下：**

```python
# 这一章节其实已经包含在上一章节中了，因此结果直接略去

age    = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weight?")
print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# 加分析题
# 1. 在命令行界面下运行你的程序，然后在命令行输入 pydoc raw_input 看它说了些什么。
# 如果你用的是 Window，那就试一下 python -m pydocraw_input 。
# 2. 输入 q 退出 pydoc。
# 3. 上网找一下 pydoc 命令是用来做什么的。
# 4. 使用 pydoc 再看一下 open, file, os, 和 sys 的含义。看不懂没关系，只要通读一下，记下你觉得有意思的点就行了。
# 这里需要了解 pydoc 是什么东西，存疑？
```



## 习题13：参数、解包、变量

**主要内容：**另外一种将参数传递给脚本的方式，也就是从外部传递的方式。

**代码以及结果如下：**

```python
from sys import argv # 从 sys 库(模组modules)中引入 argv
script, first, second, third = argv # 解包并依次赋值给左边变量
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

'''
# 接下里的需要需要在命令行中运行
# 使用 Win+R cmd 打开命令行
# 默认目录为 C盘，使用 cd /d e:\ 切换为 E盘
# cd /d E:/2018-2019_Master3/004_Py/001_笨办法学Python/NoteFor1.1-learn-python-the-hard-way/
# 有时候不用添加 /d 命令
# 可以使用 dir 命令查看当前目录下的文件
# 之后使用 python 习题13：参数、解包、变量.py first 2nd 3rd 命令，结果如下：
# The script is called: 习题13：参数、解包、变量.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
# 可以看到 对脚本传递了四个参数，脚本名和三个其他参数
'''

# 加分习题
# 1. 给你的脚本三个以下的参数。看看会得到什么错误信息。试着解释一下。
# 2. 再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些有意义的变量名。
# 3. 将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
# 4. 记住“模组(modules)”为你提供额外功能。多读几遍把这个词记住，因为我们后面还会用到它。
```

**关键技巧：**

- 掌握从命令行来将参数传递给脚本
- sys库中的argv



## 习题14：提示和传递

**主要内容：**

- 使用 argv 和 raw_input 一起来向用户提一些特别的问题，argv和input的联合使用

**代码如下：**

```python
from sys import argv
script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s scripy." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where it is.
And you have a %r computer. Nice
""" % (likes, lives, computer))

# 同样需要命令行运行
# cd /d e:\2018-2019 Master Grade 2\004_coding_file\python_file\001_Getting started\thehardway>python 习题14：提示和传递.py Zed

# 加分习题
'''
1. 查一下 Zork 和 Adventure 是两个怎样的游戏。 看看能不能下载到一版，然后玩玩看。
2. 将 prompt 变量改成完全不同的内容再运行一遍。
3. 给你的脚本再添加一个参数，让你的程序用到这个参数。
4. 确认你弄懂了三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具。
'''
```

**结果如下：**

- 这里直接将结果省略了

**关键技巧：**

- 确认你弄懂了三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具。



## 习题15：读取文件

**主要内容：**

- 读取文件，这节练习涉及到写两个文件

**代码如下：**

```python
from sys import argv    				# 调用模块
script, filename = argv 				# 对脚本读取的参数进行赋值
txt = open(filename)    				# 读取文件
print("Here's yout file %r" % filename) # 打印文件名字
print(txt.read()) 						# 打印文件内容
txt.close() 							# 关闭文件

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close() 						# 关闭文件

# 加分习题
'''
这节的难度跨越有点大，所以你要尽量做好这节加分习题，然后再继续后面的章节。
1. 在每一行的上面用注解说明这一行的用途。
2. 如果你不确定答案，就问别人，或者上网搜索。大部分时候，只要搜索 “python” 加上你要搜的东西就能得到你要的答案。比如搜索一下“python open”。
3. 我使用了“命令”这个词，不过实际上它们的名字是“函数（function）”和“方法（method）。上网搜索一下这两者的意义和区别。看不明白也没关系，迷失在别的程序员的知识海洋里是很正常的一件事情。
4. 删掉 10-15 行使用到 raw_input 的部分，再运行一遍脚本。
5. 只是用 raw_input 写这个脚本，想想那种得到文件名称的方法更好，以及为什么。
6. 运行 pydoc file 向下滚动直到看见 read() 命令（函数/方法）。看到很多别的命令了吧，你可以找几条试试看。不需要看那些包含 __ （两个下划线）的命令，这些只是垃圾而已。
7. 再次运行 python 在命令行下使用 open 打开一个文件，这种 open 和 read 的方法也值得你一学。
8. 让你的脚本针对 txt and txt_again 变量执行一下 close() ，处理完文件后你需要将其关闭，这是很重要的一点。
'''

# 对于其中的第七条
'''
Win+r cmd python 
t = open(r'e:/2018-2019 Master Grade 2/004_coding_file/python_file/001_Getting started/thehardway/ex15_example.txt') # 其中r是为了不转义
t.read()
'''

# python -m pydoc open # 命令行下查看 open 的功能
```

**结果如下：**

- 这里的结果直接省略了

**关键技巧：**

- 关于open函数的使用，可以查看帮助文档，巨详细
- 关于read函数



## 习题16：读写文件

**主要内容：**

- 一些打印的练习

**代码如下：**

```python
from sys import argv
script, filename = argv
print("We're going to erase %r." % filename)
print("If you don't want that, hit CRTL-C (^C).")
print("If you do want that, hit RETURN.")

input("?") # 这一行也可以挂起，即暂停一下，输入任意字符后回车进行，但输入的内容无意义

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# target.write("%s\n%s\n%s\n" % (line1, line2, line3)) # 这样应该更方便

print("And finally, we close it.")
target.close()

# 总结
'''
在Python中，读写文件有3个步骤：
调用open()函数，返回一个File对象。
调用File对象的read()或write()方法。
调用File对象的close()方法，关闭该文件。
'''

# 加分习题
'''
1. 如果你觉得自己没有弄懂的话，用我们的老办法，在每一行之前加上注解，为自己理清思路。就算不能理清思路，你也可以知道自己究竟具体哪里没弄明白。
2. 写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。
3. 文件中重复的地方太多了。试着用一个 target.write() 将 line1, line2, line3 打印出来，你可以使用字符串、格式化字符、以及转义字符。
4. 找出为什么我们需要给 open 多赋予一个 'w' 参数。提示： open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作。
'''
```

**结果如下：**

- 这里结果省略

**关键技巧：**

-  需要记住的关于open的命令：
   1. close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。 
   2. read – 读取文件内容。你可以把结果赋给一个变量。 
   3. readline – 读取文本文件中的一行。 
   4. truncate – 清空文件，请小心使用该命令。 
   5. write(stuff) – 将stuff写入文件。



## 习题17：更多文件操作

**主要内容：**

- 将一个文件的内容拷贝到另外一个文件中去

**代码如下：**

```python
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" % (from_file, to_file))

# we could do thess two on one line, how?
input_cac = open(from_file)
indata = input_cac.read()
# 可以写成这样：indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

output_cac = open(to_file, 'w')
output_cac.write(indata)

print("Alright, all done.")

output_cac.close()
input_cac.close()

# 命令行下使用 type 读取txt文件

# 总结：
'''
在我们调用open()时，我们输入了两个参数，第一个是要打开文件的名称，第二个是'w'。
这里，第二个参数其实是在告诉Python我们要以写入模式打开这个文件，当然还有其他的文件打开模式。
'r'读取模式
'a'附加模式（既给文件附加内容而不是覆盖内容）
'r+'读取和写入模式
默认情况下，Python将以只读模式打开文件
'''

# 加分习题
'''
1. 再多读读和 import 相关的材料，将 python 运行起来，试试这一条命令。试着看看自己能不能摸出点门道，当然了，即使弄不明白也没关系。
2. 这个脚本 实在是 有点烦人。没必要在拷贝之前问一遍把，没必要在屏幕上输出那么多东西。试着删掉脚本的一些功能，让它使用起来更加友好。
3. 看看你能把这个脚本改多短，我可以把它写成一行。
4. 我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接(con*cat*enate)”到一起，不过实际上它最大的用途是打印文件内容到屏幕上。
   你可以通过 man cat 命令了解到更多信息。
5. 使用 Windows 的同学，你们可以给自己找一个 cat 的替代品。关于 man 的东西就别想太多了，Windows 下没这个命令。
6. 找出为什么你需要在代码中写 output.close() 。
'''
```

**结果如下：**

- 不想写结果了，这些全都是一些文件操作的内容



## 习题18：命名、变量、代码、函数

**主要内容：**

- 主要是函数的学习

代码如下：

```python
# 这一章节开始学习函数

#  this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just take one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this takes no arguments
def print_none():
    print("I got nothin.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# 加分习题
'''
加分习题

为自己写一个函数注意事项以供后续参考。你可以写在一个索引卡片上随时阅读，直到你记住所有的要点为止。注意事项如下：

1.函数定义是以 def 开始的吗？
2.函数名称是以字符和下划线 _ 组成的吗？
3.函数名称是不是紧跟着括号 ( ？
4.括号里是否包含参数？多个参数是否以逗号隔开？
5.参数名称是否有重复？（不能使用重复的参数名）
6.紧跟着参数的是不是括号和冒号 ): ？
7.紧跟着函数定义的代码是否使用了 4 个空格的缩进 (indent)？
8.函数结束的位置是否取消了缩进 (“dedent”)？

当你运行（或者说“使用 use”或者“调用 call”）一个函数时，记得检查下面的要点：

1.调运函数时是否使用了函数的名称？
2.函数名称是否紧跟着 ( ？
3.括号后有无参数？多个参数是否以逗号隔开？
4.函数是否以 ) 结尾？

按照这两份检查表里的内容检查你的练习，直到你不需要检查表为止。 最后，将下面这句话阅读几遍： “‘运行函数(run)’、‘调用函数(call)’、和 ‘使用函数(use)’是同一个意思”
'''
```

**结果如下：**

```python
arg1: 'Zed', arg2: 'Shaw'
arg1: 'Zed', arg2: 'Shaw'
arg1: 'First!'
I got nothin.
```



## 习题19：函数和变量

**主要内容：**

- 关于函数的一些练习

**代码如下：**

```python
# 注意这里，函数内的两个变量都是数，因此没有使用星号 * ，而是字符串时则需要使用 * (这个结论不对)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d chesses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from out script:")
amount_of_cheeese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheeese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheeese + 100, amount_of_crackers + 1000)

# 加分习题：
'''
加分习题
1. 倒着将脚本读完，在每一行上面添加一行注解，说明这行的作用。
2. 从最后一行开始，倒着阅读每一行，读出所有的重要字符来。
3. 自己编至少一个函数出来，然后用10种方法运行这个函数。
'''
```

**结果如下：**

```python
We can just give the function numbers directly:
You have 20 chesses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from out script:
You have 10 chesses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 chesses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variable and math:
You have 110 chesses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.
```



## 习题20：函数和文件

主要内容：

- 函数和文件

代码如下：

```python
# 注意函数和文件是如何在一起发挥作用的

from sys import argv
# 从sys库中调用argv函数

script, input_file = argv
# 把argv解包，将参数依次赋值给左边的变量名

def print_all(f):
# 定义函数，形参f
    print(f.read())
    # 以只读的方式读取f中的内容并打印

def rewind(f):
# 定义函数，形参f
    f.seek(0)
    # 移动文件读取指针至f中内容的开头位置

def print_a_line(line_count, f):
# 定义函数，形参line_count和f
    print(line_count, f.readline())
    # 读取f内容的一整行，打印line_count中的内容和f中指定行的内容


current_file = open(input_file)
# 打开文件读取内容
print("First let's print the whole file:\n")
# 打印并换行 首先让我们来打印这个文件里的内容
print_all(current_file)
# 打印current_file中的内容


print("Now let's rewind, kind of like a tape.")
# 打印 现在让我们倒回去，有点像倒带
rewind(current_file)
# 将文件读取指针移至开头位置


print("Let's print three lines:")
# 打印 让我们打印三行
current_line = 1
# 设置读取的行数为第一行
print_a_line(current_line, current_file)
# 打印文件内容的第一行
current_line = current_line + 1
# 行数增加1，即读取第二行
print_a_line(current_line, current_file)
# 打印文件内容的第二行
current_line = current_line + 1
# 行数再增加1，即读取第三行
print_a_line(current_line, current_file)
# 打印文件内容的第三行

# 总结
'''
from http://blog.chinaunix.net/uid-26990529-id-3405843.html 
import
#导入mode，import与from…import的不同之处在于，简单说：
# 如果你想要直接输入argv变量到你的程序中而每次使用它时又不想打sys，
# 则可使用：from sys import argv
# 一般说来，应该避免使用from..import而使用import语句，
# 因为这样可以使你的程序更加易读，也可以避免名称的冲突

from sys import argv (用 argv)
import sys (用 sys.argv)
'''

# 加分习题
'''
1. 通读脚本，在每行之前加上注解，以理解脚本里发生的事情。
2. 每次 print_a_line 运行时，你都传递了一个叫 current_line 的变量。在每次调用函数时，打印出 current_line 的至，
   跟踪一下它在print_a_line 中是怎样变成 line_count 的。
3. 找出脚本中每一个用到函数的地方。检查 def 一行，确认参数没有用错。
4. 上网研究一下 file 中的 seek 函数是做什么用的。试着运行 pydoc file 看看能不能学到更多。
5. 研究一下 += 这个简写操作符的作用，写一个脚本，把这个操作符用在里边试一下。
'''
```



## 习题21：函数可以返回东西

**主要内容：**

- 函数返回值

**代码如下：**

```python
# 利用 = 给变量赋值，以及利用 return 返回函数值

def add(a, b):
    print("ADDING %d + %d" % (a,b))
    return(a + b)

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return(a - b)

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return(a * b)

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return(a / b)

print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, Iq: %d" % (age, height, weight, iq))

#  A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?") # int(what) 可以将 浮点数 转换为 整数

# 加分习题
'''
1. 如果你不是很确定 return 的功能，试着自己写几个函数出来，让它们返回一些值。你可以将任何可以放在 = 右边的东西作为一个函数的返回值。
2. 这个脚本的结尾是一个迷题。我将一个函数的返回值用作了另外一个函数的参数。我将它们链接到了一起，就跟写数学等式一样。这样可能有些难读，不过运行一下你就知道结果了。
   接下来，你需要试试看能不能用正常的方法实现和这个表达式一样的功能。
3. 一旦你解决了这个迷题，试着修改一下函数里的某些部分，然后看会有什么样的结果。你可以有目的地修改它，让它输出另外一个值。
4. 最后，颠倒过来做一次。写一个简单的等式，使用一样的函数来计算它。
这个习题可能会让你有些头大，不过还是慢慢来，把它当做一个游戏，解决这样的迷题正是编程的乐趣之一。后面你还会看到类似的小谜题。
'''
```

**结果如下：**

```python
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, Iq: 50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391.0 Can you do it by hand?
```



## 习题22：到现在你学到了哪些东西

**主要内容：**

- 复习总结

**总结要点：**（以下是来自一位网友的总结）

```python
print() 			# 打印内容
input() 			# 输入内容
form ... import ... # 从模组中引入函数方法
import 				# 引入导入
argv 				# 参数变量
open() 				# 打开指定文件
read() 				# 读取文件内容
close() 			# 关闭被打开的文件并把保存
readline 			# 读取文本文件中的一行
runcate 			# 清空文件，请小心使用该命令
write(stuff) 		# 将stuff写入文件
exists(path) 		# 路径判断，存在返回True，路径损坏返回False
def 				# 定义一个函数
seek() 				# 文件指针，移动文件读取指针至指定位置
return() 			# 返回，将变量值返回，作为函数的值
```



## 习题23：读代码

**主要内容：**

- 读代码

**关键技巧：**

- 这里可以选择之前那个chineseChess的代码



## 习题24：更多练习

**主要内容：**

- 主要是对全书前半部分的一个总结练习

**代码如下：**

```python
print("Let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do \n newlines and \t tabs")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars /100
    return(jelly_beans, jars, crates)

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))

# 加分习题
'''
1. 记得仔细检查结果,从后往前倒着检查,把代码朗读出来,在不清楚的位置加上注释。
2. 故意把代码改错,运行并检查会发生什么样的错误,并且确认你有能力改正这些错误。
'''
```

**结果如下：**

```python
Let's practice everything.
You'd need to know 'bout escapes with \ that do 
 newlines and 	 tabs
--------------

	The lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

		where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans, 50000 jars, and 500 crates.
We can also do that this way:
We'd have 500000 beans, 5000 jars, and 50 crates.
```



## 习题25：更多更多的练习

**主要内容：**

- 一些关于函数和变量的练习

**代码如下：**

```python
# 这节是一些函数和变量的练习

def break_words(stuff):
    # 将句子拆分为单词
    """This function will break up words for us."""
    words = stuff.split(' ')
    return(words)

def sort_words(words):
    # 对若干个单词排序
    """Sort the words."""
    return(sorted(words))

def print_first_word(words):
    # 将第一个单词打印出来并弹出
    """Prints the first world after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    # 将最后一个单词打印出来并弹出
    """Prints the last word after popping it pff"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    # 将句子拆分为多个单词，并且排序
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return(sort_words(words))

def print_first_and_last(sentence):
    # 将句子拆分为多个单词，打印首尾两个单词并将他们弹出
    """Prints the first and the last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    # 将句子拆分为多个单词并排序，打印首尾两个单词并淡出
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# 在命令行中操作为
'''
cd /d e:/2018-2019 Master Grade 2/004_coding_file/python_file/001_Getting started/thehardway
python
import ex25 # 这里要想运行应该将中文文件名改为 ex25.py
sentence = "All good things come to those who wait."
sentence
words = ex25.break_words(sentence)
words
sorted_words = ex25.sort_words(words)
sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words
ex25.sort_sentence(sentence)
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
'''

# 注意
# 用命令行打开时，应保证文件名为中文
# 将当前文件夹选定为当前文件所在的文件下
# 修改 ex25.py 后应该重新导入 import ex25， 有必要的话应该重新启动 cmd

# 加分习题
'''
1.研究答案中没有分析过的行，找出它们的来龙去脉。确认自己明白了自己使用的是 模组 ex25 中定义的函数。
2.试着执行 help(ex25) 和 help(ex25.break_words) 。这是你得到模组帮助文档的方式。 所谓帮助文档就是你定义函数时放在 """ 之间的东西，
  它们也被称作 documentation comments （文档注解），后面你还会看到更多类似的东西。 
3.重复键入 ex25. 是很烦的一件事情。有一个捷径就是用 from ex25 import * 的方式导入模组。这相当于说： “我要把 ex25 中所有的东西 import 进来。
  ”程序员喜欢说这样的倒装句，开一个新的会话，看看你所有的函数是不是已经在那里了。 
4.把你脚本里的内容逐行通过 python 编译器执行，看看会是什么样子。你可以执行CTRL-D (Windows 下是 CTRL-Z)来关闭编译器。
'''
```

**结果如下：**

- 没有结果，是在命令行中操作的



## 习题26：恭喜你，现在可以考试了！

**主要内容：**

- 修改存在错误的程序

**代码如下：**

```python
# 说明
'''
在这节练习中，你将面对一个水平糟糕的程序员，并改好他的代码。我将习题 24和 25 胡乱拷贝到了一个文件中，
随机地删掉了一些字符，然后添加了一些错误进去。大部分的错误是 Python 在执行时会告诉你的，还有一些算术错误是你要自己找出来的。
再剩下来的就是格式和拼写错误了。

所有这些错误都是程序员很容易犯的，就算有经验的程序员也不例外。你的任务是将此文件修改正确，用你所有的技能改进这个脚本。
你可以先分析这个文件，或者你还可以把它像学期论文一样打印出来，修正里边的每一个缺陷，重复修正和运行的动作，直到这个脚本可以完美地运行起来。
在整个过程中不要寻求帮助，如果你卡在某个地方无法进行下去，那就休息一会晚点再做。

就算你需要几天才能完成，也不要放弃，直到完全改对为止。最后要说的是，这个练习的目的不是写程序，而是修正现有的程序。
'''

# 原版
'''
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates == secret_formula(start-point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
.print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
prin sorted_words

print_irst_and_last(sentence)

   print_first_a_last_sorted(senence)
'''

# 修改版
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(stuff)
    return(words)

def sort_words(words):
    """Sorts the words."""
    return(sorted(words))

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return(sort_words(words))

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %d" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return(jelly_beans, jars, crates)

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
# prin sorted_words

print_first_and_last(sentence)
print_first_and_last_sorted(senence)
```



## 习题27：记住逻辑关系

**主要内容：**

- 掌握基本的逻辑关系
- 这一小节没有代码

**关键技巧：**（掌握常见的逻辑关系）

- 与或非
- 等于，不等于
- 大于，小于，大于等于，小于等于
- 真，假





## 习题28：布尔表达式练习

**主要内容：**

- 练习布尔表达式

**代码如下：**

```python
test=[
True and True,  				# 1
False and True, 				# 0 
1 == 1 and 2 == 1, 				# 0
"test" == "test", 				# 1
1 == 1 or 2 != 1, 				# 1
True and 1 == 1, 				# 1
False and 0 != 0, 				# 0
True or 1 == 1, 				# 1
"test" == "testing", 			# 0
1 != 0 and 2 == 1, 				# 0
"test" != "testing", 			# 1
"test" == 1, 					# 0
not (True and False), 			# 1 
not (1 == 1 and 0 != 1), 		# 0 
not (10 == 1 or 1000 == 1000), 	# 0
not (1 != 10 or 3 == 4), 		# 0
not ("testing" == "testing" and "Zed" == "Cool Guy"), 			# 1
1 == 1 and not ("testing" == 1 or 1 == 0), 						# 1
"chunky" == "bacon" and not (3 == 4 or 3 == 3), 				# 0
3 == 3 and not ("testing" == "testing" or "Python" == "Fun"), 	# 0
]

print(test)
```

**结果如下：**

```python
[True, False, False, True, True, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False]
```



## 习题29：如果（if）

**主要内容：**

- 学习if条件判断

**代码如下：**

```python
people = 20
cats   = 30
dogs   = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:

    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")

# 加分习题
'''
猜猜“if 语句”是什么，它有什么用处。在做下一道习题前，试着用自己的话回答 下面的问题:
1.你认为 if 对于它下一行的代码做了什么？
2.为什么 if 语句的下一行需要 4 个空格的缩进？
3.如果不缩进，会发生什么事情？
4.把习题 27 中的其它布尔表达式放到``if 语句``中会不会也可以运行呢？试一下。
如果把变量 people, cats, 和 dogs 的初始值改掉，会发生什么事情？
'''
```

**结果如下：**

```python
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
```



## 习题30：Else 和 If

**主要内容：**

- 学习if-else语句

**代码如下：**

```python
people = 30
cars   = 40
buses  = 15

if cars > people:
    print("We should take the cars.")
elif cars > people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That't too many buses.")
elif buses < cars:
    print("Maybe we could take buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")

# 加分习题
'''
1.猜想一下 elif 和 else 的功能。
2.将 cars, people, 和 buses 的数量改掉，然后追溯每一个 if 语句。看看最后会 打印出什么来。
3.试着写一些复杂的布尔表达式，例如 cars > people and buses < cars。
4.在每一行的上面写注解，说明这一行的功用。
'''
```

**结果如下：**

```python
We should take the cars.
Maybe we could take buses.
Alright, let's just take the buses.
```



## 习题31：作出决定

**主要内容：**

- 开始创建包含条件判断的脚本

**代码如下：**

  ```python
print("You enter a dark room with doors. Do you go through door #1 or door #2?")
door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthultu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins,")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mine of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good Job!")

# 加分习题
'''
为游戏添加新的部分，改变玩家做决定的位置。尽自己的能力扩展这个游戏，不过别把游戏弄得太怪异了。
'''
  ```

**结果如下：**

- 结果需要交互演示



## 习题32：循环和列表

**主要内容：**

- 学习循环和列表

**代码如下：**

```python
hairs  = ['brown', 'blond', 'red']
eyes   = ['brown', 'blue', 'green']
weight = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits    = ['apples', 'oranges', 'pears', 'apricots']
change    = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list." % i)
    elements.append(i)

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)

# 加分习题
'''
1. 注意一下 range 的用法。查一下 range 函数并理解它。
2. 在第 22 行，你可以直接将 elements 赋值为 range(0,6)，而无需使用 for 循环？
3. 在 Python 文档中找到关于列表的内容，仔细阅读以下，除了 append 以外列表还 支持哪些操作？
'''
```

**结果如下：**

```python
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
```



## 习题33：While 循环

**主要内容：**

- 学习while循环

**代码如下：**

```python
i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

# 加分习题
'''
1.将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。
2.使用这个函数重写你的脚本，并用不同的数字进行测试。
3.为函数添加另外一个参数，这个参数用来定义第 8 行的加值 + 1 ，这样你就可以 让它任意加值了。
4.再使用该函数重写一遍这个脚本。看看效果如何。
5.接下来使用 for-loop 和 range 把这个脚本再写一遍。你还需要中间的加值操作吗？如果你不去掉它，会有什么样的结果？
'''

# 首先写成一个函数，输入数字 i，返回一个列表 0-i-1
def number_list1(j):
    i = 0
    numbers = []
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
number_list1(6)

# 首先写成一个函数，输入数字 j,n，返回一个列表 0-i-1 中 步进为 n
def number_list2(j, n):
    i = 0
    numbers = []
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + n
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
number_list2(6, 2)

# 改用for-loop实现 0到j-1 的任意步进 n(其实就是range函数功能)
def number_list3(j, n):
    numbers = range(0, j, n)
    for i in range(0, len(numbers)):
        print(numbers[i])
number_list3(6,2)

# 特别注意
'''range的结果是一个序列，而非列表，因此不能直接输出
'''
print(range(0, 6))
print(list(range(0, 6)))

# 以下关于 while 的工作继续
# 使用 break 和 continue 退出循环

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

# 可以改成
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

**结果如下：**

```python
At the top i is 0
Numbers now:  [0]
At the bottom i is 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now:  [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5
At the top i is 0
Numbers now:  [0]
At the bottom i is 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now:  [0, 1, 2, 3, 4, 5]
At the bottom i is 6
At the top i is 0
Numbers now:  [0]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 2]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 2, 4]
At the bottom i is 6
0
2
4
range(0, 6)
[0, 1, 2, 3, 4, 5]
1
3
5
7
9
1
3
5
7
9
```

**关键技巧：**

- range函数的使用，借助帮助文档进行查看



## 习题34：访问列表的元素

**主要内容：**

- 如何访问列表中的元素

**代码如下：**

```python
animals = ['bear','python','peacock','kangaroo','whale','platypus'] 
# 与序号相对应的每位选手的信息
# 列出每行制定动物在animals列表中的基数
name_number = [1,2,0,3,4,2,5,4] # 序号，即几号选手
ordinal = [2,3,1,4,5,3,6,5] 	# 每位选手的名次
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
```

**结果如下：**

```python
The 2nd animal is at 1 and is a python
The 3rd animal is at 2 and is a peacock
The 1st animal is at 0 and is a bear
The 4th animal is at 3 and is a kangaroo
The 5th animal is at 4 and is a whale
The 3rd animal is at 2 and is a peacock
The 6th animal is at 5 and is a platypus
The 5th animal is at 4 and is a whale

Turn Around: 

The animal at 1 is the 2nd animal and is a python
The animal at 2 is the 3rd animal and is a peacock
The animal at 0 is the 1st animal and is a bear
The animal at 3 is the 4th animal and is a kangaroo
The animal at 4 is the 5th animal and is a whale
The animal at 2 is the 3rd animal and is a peacock
The animal at 5 is the 6th animal and is a platypus
The animal at 4 is the 5th animal and is a whale
```



## 习题35：分支和函数

**主要内容：**

- 学习分支和函数

**代码如下：**

```python
from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next: # 也就是说输入的数字中必须有 0 或者 1
        how_much = int(next)
    else:
        dead ("Man, learn to type a number.")
    
    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit (0)
    else:
        dead ("You greedy bastard!") # 你这贪婪的混蛋

def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.") # 熊有一堆蜂蜜
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        next = input("> ")
        
        if next == "take honey":
            dead ("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved: # 嘲讽熊
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead ("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")

def cthuhu_room():
    print ("Here you see the great evil Cthulhu.") # 邪恶的克苏鲁
    print ("He, it, whatever stares at you and you go insane.") # 他，无论什么盯着你，你都疯了
    print ("Do you flee for your life or eat your head?") # 你是逃命还是吃头？
    
    next = input("> ")
    
    if "flee" in next:
        start() # 这里重新回到开始的地方
    elif "head" in next:
        dead ("Well that was tasty!")
    else:
        cthuhu_room()

def dead(why):
    print (why, "Good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")
    
    next = input("> ")
    
    if next == "left":
        bear_room() # 熊房间
    elif next == "right":
        cthuhu_room() # 邪神房间
    else:
        dead ("You stumble around the room until you starve.")
        # 你在房间里绊倒直到你饿死（这也太恶毒了吧）
       
start()

# 这游戏挺有意思的啊

# 加分习题
'''
1.把这个游戏的地图画出来，把自己的路线也画出来。
2.改正你所有的错误，包括拼写错误。
3.为你不懂的函数写注解。记得文档注解该怎么写吗？
4.为游戏添加更多元素。通过怎样的方式可以简化并且扩展游戏的功能呢？
5.这个 gold_room 游戏使用了奇怪的方式让你键入一个数字。这种方式会导致什么样的 bug？
  你可以用比检查 0、1 更好的方式判断输入是否是数字吗？int() 这个函数可以给你一些头绪。
'''
```

**结果如下：**

- 结果需要人机交互



## 习题36：设计和调试

**主要内容：**

- 设置一个分支类型的文字游戏
- 这个可以跳过了



## 习题37：复习各种符号

**主要内容：**

- 关键字
- 数据类型
- 字符串转义序列
- 字符串格式化
- 操作符号



## 习题38：阅读代码

**主要内容：**

- 阅读代码
- 这个也是暂时跳过了




## 习题39：列表的操作

**主要内容：**

- 关于列表的一些操作

**代码如下：**

```python
# 示例1
class Thing(object):
    def test(hi):
        print("hi")
    
a = Thing()
a.test()

# 示例2
class Thing(object):
    def test(a,hi):
        print("hi")
    
a = Thing()
a.test("hello")

# 练习
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Gril", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ",next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))
print("There we go: ", stuff)

print("Let's do some things with stuff.")
print(stuff[1]) # 第二个
print(stuff[-1]) # 最后一个
print(stuff.pop()) # 弹出最后一个
print(' '.join(stuff)) # 用空格字符连接，注意最后一个cron已经弹出
print('#'.join(stuff[3:5])) # 用 # 连接 3 4 两个序号的单词

# 加分习题
'''
1. 将每一个被调用的函数以上述的方式翻译成 Python 实际执行的动作。例如：'
'.join(things) 其实是 join(' ', things) 。
2. 将这两种方式翻译为自然语言。例如，' '.join(things) 可以翻译成“用 ‘ ‘ 连接
(join) things”，而 join(' ', things) 的意思是“为 ‘ ‘ 和 things 调用 join 函数”。
这其实是同一件事情。
3. 上网阅读一些关于“面向对象编程 (Object Oriented Programming)”的资料。晕了
吧？嗯，我以前也是。别担心。你将从这本书学到足够用的关于面向对象编程的基
础知识，而以后你还可以慢慢学到更多。
4. 查一下 Python 中的 “class” 是什么东西。不要阅读关于其他语言的 “class” 的用法，
这会让你更糊涂。
5. dir(something) 和 something 的 class 有什么关系？
6. 如果你不知道我讲的是些什么东西，别担心。程序员为了显得自己聪明，于是
就发明了 Object Oriented Programming，简称为 OOP，然后他们就开始滥用这
个东西了。如果你觉得这东西太难，你可以开始学一下“函数编程 (functional
programming)”。
'''
```

**结果如下：**

```python
hi
hi
Wait there's not 10 things in that list, let's fix that.
Adding:  Boy
There's 7 items now.
Adding:  Gril
There's 8 items now.
Adding:  Banana
There's 9 items now.
Adding:  Corn
There's 10 items now.
There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Gril', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Gril Banana
Telephone#Light
```

关键技巧：

- 关于列表的一些函数
- append，pop
- 使用joiin来连接字符串




## 习题40：字典，可爱的字典

**主要内容：**

- 学习关于字典的操作

**代码如下：**

```python
# --------------------------
things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

# ---------------------------
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "San Francisco"
print(stuff['city'])

# ---------------------------
stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
print(stuff)

# ---------------------------
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

# ---------------------------
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return(themap[state])
    else:
        return("Not found.")

# ok pay attention!
cities['_find'] = find_city # 把函数放到了字典里

while True:
    print("State? (ENTER to quit)")
    state = input("> ")

    if not state: break # 这里直接回车则 input 接受到的为空或者0， not state 为 True

    # this line is the most important ever! study!
    city_found  = cities['_find'](cities, state) # 用字典中的函数来寻找 state
    print(city_found)

# 加分习题
'''
1. 在 Python 文档中找到 dictionary (又被称作 dicts, dict) 的相关的内容，学着对 dict做更多的操作。
2. 找出一些 dict 无法做到的事情。例如比较重要的一个就是 dict 的内容是无序的，你可以检查一下看看是否真是这样。
3. 试着把 for-loop 执行到 dict 上面，然后试着在 for-loop 中使用 dict 的 items() 函数，看看会有什么样的结果。
'''
```

**结果如下：**

```python
b
z
['a', 'z', 'c', 'd']
Zed
36
74
San Francisco
Wow
Neato
{'name': 'Zed', 'age': 36, 'height': 74, 'city': 'San Francisco', 1: 'Wow', 2: 'Neato'}
{'name': 'Zed', 'age': 36, 'height': 74}
State? (ENTER to quit)

# 以下需要人机交互了
```




## 习题41：来自 Percal 25 号行星的哥顿人

**主要内容：**

- 一个更加复杂的条件分支类型的文字游戏
- 程序过长，因此这里就不列出了



## 习题42：物以类聚

**主要内容：**

- 学习关于类的知识

**代码如下：**

```python
# 之前的例子

stuff = ['Test', 'This', 'Out']
print(' '.join(stuff))

class TheThing(object):
    # self 是一个默认的隐含参数，即对象（物体）本身s
    def __init__(self): # 这里创建对象即进行初始化的内容，可以看到创建对象不需要传递参数
        self.number = 0
    
    def some_function(self):
        print("I got called.")
    
    def add_me_up(self, more): # 
        self.number += more
        return(self.number)

# two things
a = TheThing()
b = TheThing()

a.some_function() # 这里是不能加任何参数的
b.some_function()

print(a.add_me_up(20)) # 这里只能有一个参数
print(b.add_me_up(30))

print(a.number)
print(b.number)

# Study this. This is how you pass a variable
# from one class to another. You will need this.

class TheMultiplier(object):

    def __init__(self, base):# 这里进行初始化，可以看到创建对象需要传递一个参数
        self.base = base
    def do_it(self, m):
        return(m*self.base)

x = TheMultiplier(a.number) # 体会一下这里
print(x.do_it(b.number)) # 体会一下参数的个数
    
# 接下来将习题41的题用类重写一遍
'''
这么麻烦的吗？？？
'''

from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud. If she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print("\n--------")
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)

    def central_corridor(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an ")
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        action = input("> ")

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your laser hits his costume but misses him entirely. This")
            print("completely ruins his brand new costume his mother bought him, which")
            print("makes him fly into an insane rage and blast you repeatedly in the face until")
            print("you are dead. Then he eats you.")
            return('death')

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you.")
            return('death')

        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
            print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return('laser_weapon_armory')

        else:
            print("DOES NOT COMPUTE!")
            return('central_corridor')

    def laser_weapon_armory(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb. The code is 3 digits.")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return('the_bridge')
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return('death')

    def the_bridge(self):
        print("You burst onto the Bridge with the netron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. Each of them has an even uglier")
        print("clown costume than the last. They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            print("As you die you see another Gothon frantically try to disarm")
            print("the bomb. You die knowing they will probably blow up when")
            print("it goes off.")
            return('death')

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return('escape_pod')

        else:
            print("DOES NOT COMPUTE!")
            return("the_bridge")

    def escape_pod(self):
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes. It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference. You get to the chamber with the escape pods, and")
        print("now need to pick one to take. Some of them could be damaged")
        print("but you don't have time to look. There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return('death')
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time. You won!")
            exit(0)

a_game = Game("central_corridor")
a_game.play()

# 加分习题
'''
1. 解释一下返回至下一个房间的工作原理。
2. 创建更多的房间，让游戏规模变大。
3. 除了让每个函数打印自己以外，再学习一下“文档字符串 (doc strings)”式的注解。
   看看你能不能将房间描述写成文档注解，然后修改运行它的代码，让它把文档注解打印出来。
4. 一旦你用了文档注解作为房间描述，你还需要让这个函数打印出用户提示吗？试着
   让运行函数的代码打出用户提示来，然后将用户输入传递到各个函数。你的函数应
   该只是一些 if 语句组合，将结果打印出来，并且返回下一个房间。
5. 这其实是一个小版本的“有限状态机 (finite state machine)”，找资料阅读了解一下，
   虽然你可能看不懂，但还是找来看看吧。
6. 我的代码里有一个 bug，为什么门锁要猜测 11 次？
'''
```



## 习题43：你来制作一个游戏

- 略
- 以下就都省略了，等以后有时间再刷的时候来补一遍吧



## 习题44：给你的游戏打分

- 略



## 习题45：对象、类、以及从属关系

- 略



## 习题46：一个项目骨架

- 略



## 习题47：自动化测试

- 略



## 习题48：更复杂的用户输入

- 略



## 习题49：创建句子

- 略



## 习题50：你的第一个网站

- 略



## 习题51：从浏览器中获取输入

- 略



## 习题52：创建你的 web 游戏

- 略



## 下一步

- 略



## 老程序员的建议

- 略



## Indices and tables

- 略