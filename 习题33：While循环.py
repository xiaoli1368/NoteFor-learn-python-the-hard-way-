# 接下来是 while-loop 循环
'''
While 循环有一个问题，那就是有时它会永不结束。如果你的目的是循环到宇宙 毁灭为止，那这样也挺好的，
不过其他的情况下你的循环总需要有一个结束点。

为了避免这样的问题，你需要遵循下面的规定：
1.尽量少用 while-loop，大部分时候 for-loop 是更好的选择。
2.重复检查你的 while 语句，确定你测试的布尔表达式最终会变成 False 。
3.如果不确定，就在 while-loop 的结尾打印出你要测试的值。看看它的变化。
'''

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

# 加分习题
'''
1.将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。
2.使用这个函数重写你的脚本，并用不同的数字进行测试。
3.为函数添加另外一个参数，这个参数用来定义第 8 行的加值 + 1 ，这样你就可以 让它任意加值了。
4.再使用该函数重写一遍这个脚本。看看效果如何。
5.接下来使用 for-loop 和 range 把这个脚本再写一遍。你还需要中间的加值操作吗？如果你不去掉它，会有什么样的结果？
'''

# 首先写成一个函数，输入数字 i，返回一个列表 0-i-1
def number_list1(j):
    i = 0
    numbers = []
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
number_list1(6)

# 首先写成一个函数，输入数字 j,n，返回一个列表 0-i-1 中 步进为 n
def number_list2(j, n):
    i = 0
    numbers = []
    while i < j:
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + n
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)
number_list2(6, 2)

# 改用for-loop实现 0到j-1 的任意步进 n(其实就是range函数功能)
def number_list3(j, n):
    numbers = range(0, j, n)
    for i in range(0, len(numbers)):
        print(numbers[i])
number_list3(6,2)

# 特别注意
'''range的结果是一个序列，而非列表，因此不能直接输出
'''
print(range(0, 6))
print(list(range(0, 6)))

# 以下关于 while 的工作继续
# 使用 break 和 continue 退出循环

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

# 可以改成
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)