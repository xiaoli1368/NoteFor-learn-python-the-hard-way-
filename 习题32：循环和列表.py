'''
在你开始使用 for 循环之前，你需要在某个位置存放循环的结果。最好的方法是使用列表(list)，
顾名思义，它就是一个按顺序存放东西的容器。列表并不复杂，你只是要学习一点新的语法。
首先我们看看如何创建列表：
'''

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weight = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

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