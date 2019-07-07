# 需要记住的的命令
'''
close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。 
read – 读取文件内容。你可以把结果赋给一个变量。 
readline – 读取文本文件中的一行。 
truncate – 清空文件，请小心使用该命令。 
write(stuff) – 将stuff写入文件。
'''

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