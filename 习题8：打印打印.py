formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
# 注意用都逗号分隔，并且最后一处没有逗号

# 加分习题
# 1.自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯同样的错误
# 2.注意最后一行中既有单引号又有双引号，你觉得它是如何工作的？

# 为了区分 %r 和 %s 的区别，可以另外赋值
formatter = "%s %s %s %s"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))