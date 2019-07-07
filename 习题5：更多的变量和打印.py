# 现在要键入更多的变量并且把他们打印出来
# 这里我们将使用一个叫“格式化字符串（format string）”的东i

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 75 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'Whith'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
# this line is tricky, and try to get it exactly right.
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# 加分习题
# 1.修改所有变量的名字，把他们前边的”my_“去掉。确认将每一个地方都去掉。

# 2.试着使用更多的格式化字符。例如 %r 就是一个非常有用的一个
# 它的含义是，不管什么都打印出来

# 3.在网上搜索所有的Python格式化字符

# 4.试着用变量将英寸和磅转换成厘米和千克。不要直接键入答案，
# 使用Python的计算功能来完成