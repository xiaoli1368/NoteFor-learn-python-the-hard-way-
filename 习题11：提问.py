# 这一章节主要使用 输入input()

print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weigh")
weight = input()
print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# 这里注意到输入光标在语句的下方，可以使用下种形式：
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")
print("So, you're %s old, %s tall and %s heavy." % (age, height, weight))

# 加分习题
# 1.上网查询Python的raw_input实现的是什么功能？
# 2.你能找到它的别的用法吗？测试一下你上网搜到的例子。
# 3.用类似的格式再写一段，把问题改成你自己的问题。
# 4.和转义序列有关的，想想为什么最后一行 '6\2"' 里边有一个 \' 序列
# 单引号需要被转义，从而防止它被识别为字符串的结尾。有没有注意到这一点？

# 注意这里将第二组的输出改为了 %s ，注意与 %r 的区别