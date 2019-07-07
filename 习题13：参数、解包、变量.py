# 介绍将变量传递给脚本的方法
# 脚本就是你自己些的 .py 文件，参数就是 argument

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
# cd /d e:/2018-2019 Master Grade 2/004_coding_file/python_file/001_Getting started/thehardway/
# 可以使用 dir 命令查看当前目录下的文件
# 之后使用 python 习题13：参数、解包、变量.py first 2nd 3rd 命令，结果如下：
# The script is called: 习题13：参数、解包、变量.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
# 可以看到 对脚本传递了四个参数，脚本名和三个其他参数
'''

# 当运行脚本时提供的参数个数不对时，会报错 need more than 3 values to unpack
'''
Traceback (most recent call last):
  File "习题13：参数、解包、变量.py", line 5, in <module>
    script, first, second, third = argv # 解包并依次赋值给左边变量
ValueError: not enough values to unpack (expected 4, got 3)
'''

# 加分习题
'''
1. 给你的脚本三个以下的参数。看看会得到什么错误信息。试着解释一下。
2. 再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些有意义的变量名。
3. 将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
4. 记住“模组(modules)”为你提供额外功能。多读几遍把这个词记住，因为我们后面还会用到它。
'''