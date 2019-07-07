# 本章节使用 argv 和 raw_input 一起来向用户提一些特别的问题

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