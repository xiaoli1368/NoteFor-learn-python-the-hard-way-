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