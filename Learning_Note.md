# Learning Notes

作者：xiaoli1368
日期：2019/07/16
字数：10k




## 前言

> 这是《笨办法学Python 2.0》的学习笔记，主要是关于每一小节的技巧。



## 目录

[TOC]

## 习题0：准备工作

本节主要内容是**Python环境的配置**，当前我所使用的是Window环境，所需要的软件有：

- windown10 1809
- Python 3.6.4
- VsCode 1.36.1

配置步骤简述如下：

- 去[官网](https://www.python.org/)下载对应版本的Python并安装，配置环境变量，使用命令行验证是否成功安装
- 去[官网](https://code.visualstudio.com/)下载VsCode并安装，下载Python插件并配置
- 测试代码

使用CMD运行python的结果如下：

```python
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>python
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Ana
conda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

这里需要注意的一些技巧：

1. 使用命令行CMD以及PowerShell
2. 熟悉命令行下的一些操作



## 习题1：第一个程序

本节主要内容是使用print函数打印字符串

代码如下：

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

结果如下：

```python
'''

'''
```











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

特殊的技巧：

- 结尾不换行
- 打印含有转移字符的字符串
- 格式化输出
- 关于输出中文 # --coding:utf-8--



## 习题2：注释和井号

本节的要点包括：

- 使用井号进行注释
- 使用三个单引号或者双引号进行注释
- 在VsCode中注释的快捷键是 ctrl+k c，取消注释的快捷键是 ctrl+k u



## 习题3：数字和数字计算

注意：

- 双除号表示向下取整，精度保持一致
- 关于转义字符
- print使用三引号打印
- 使用 %r 来格式化字符串
- pydoc的命令
- 习题13：参数、解包、变量
- Zork 和 Adventure 是两个怎样的游戏
- 习题15：读取文件
- 习题16：读写文件
- 习题17：更多文件操作



## 习题4：变量和命令

- 变量命名，驼峰准则



## 习题5：更多的变量和打印

- 格式化字符串 format string
-  试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什
  么都打印出来”。



## 习题6：更多打印

- 这一节主要是打印的联系



## 习题7：打印，打印

- 一些格式化输出字符串的特殊形式



## 习题9：打印，打印，打印

- 一些打印的练习



## 习题10：那是什么？

- 转义字符
- 三引号

## 习题11：提问

- 关于input的使用



## 习题12：提示别人

- 关于input的使用



## 习题13：参数、解包、变量

- 从命令行来将参数传递给脚本



## 习题14：提示和传递

- argv和input的联合使用



## 习题15：读取文件

- 一些打印的练习



## 习题16：读写文件

- 一些打印的练习



## 习题17：更多文件操作

- 一些打印的练习



## 习题18：命名、变量、代码、函数

- 一些打印的练习



## 习题19：函数和变量

- 一些打印的练习



## 习题20：函数和文件

- 一些打印的练习



## 习题21：函数可以返回东西

- 一些打印的练习



## 习题22：到现在你学到了哪些东西

- 一些打印的练习



## 习题23：读代码

- 一些打印的练习



## 习题24：更多练习

- 一些打印的练习



## 习题25：更多更多的练习

- 一些打印的练习



## 习题26：恭喜你，现在可以考试了！

- 一些打印的练习



## 习题27：记住逻辑关系

- 一些打印的练习



## 习题28：布尔表达式练习

- 一些打印的练习



## 习题29：如果（if）

- 一些打印的练习



## 习题30：Else 和 If

- 一些打印的练习



## 习题31：作出决定

- 一些打印的练习



## 习题32：循环和列表

- 一些打印的练习



## 习题33：While 循环

- 一些打印的练习



## 习题34：访问列表的元素

- 一些打印的练习



## 习题35：分支和函数

- 一些打印的练习



## 习题36：设计和调试

- 一些打印的练习



## 习题37：复习各种符号

- 一些打印的练习



## 习题38：阅读代码

- 一些打印的练习




## 习题39：列表的操作

- 一些打印的练习




## 习题40：字典，可爱的字典

- 一些打印的练习




## 习题41：来自 Percal 25 号行星的哥顿人

- 一些打印的练习



## 习题42：物以类聚

- 一些打印的练习



## 习题43：你来制作一个游戏

- 一些打印的练习



## 习题44：给你的游戏打分

- 一些打印的练习



## 习题45：对象、类、以及从属关系

- 一些打印的练习



## 习题46：一个项目骨架

- 一些打印的练习



## 习题47：自动化测试

- 一些打印的练习



## 习题48：更复杂的用户输入

- 一些打印的练习



## 习题49：创建句子

- 一些打印的练习



## 习题50：你的第一个网站

- 一些打印的练习



## 习题51：从浏览器中获取输入

- 一些打印的练习



## 习题52：创建你的 web 游戏

- 一些打印的练习



## 下一步

- 一些打印的练习



## 老程序员的建议

- 一些打印的练习



## Indices and tables

- 一些打印的练习



## 一些小技巧

1. 逗号后面必加空格
2. 运算符前后必加空格
3. 变量命名，驼峰准则
4. 源代码先写注释
5. 代码块之间以两个空格为分隔，单个代码块之间以单个空格为分隔
6. 

































