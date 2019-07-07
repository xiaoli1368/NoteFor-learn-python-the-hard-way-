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