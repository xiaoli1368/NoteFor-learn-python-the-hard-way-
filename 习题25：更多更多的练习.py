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