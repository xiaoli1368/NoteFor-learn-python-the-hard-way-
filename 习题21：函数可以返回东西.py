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