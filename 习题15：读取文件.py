# 这节练习涉及到写两个文件

from sys import argv # 调用模块
script, filename = argv # 对脚本读取的参数进行赋值
txt = open(filename) # 读取文件
print("Here's yout file %r" % filename) # 打印文件名字
print(txt.read()) # 打印文件内容
txt.close() # 关闭文件

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close() # 关闭文件

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