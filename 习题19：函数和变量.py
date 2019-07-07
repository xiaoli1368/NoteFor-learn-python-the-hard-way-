# 关于函数和变量的一些简单练习

# 注意这里，函数内的两个变量都是数，因此没有使用星号 * ，而是字符串时则需要使用 *
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d chesses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from out script:")
amount_of_cheeese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheeese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheeese + 100, amount_of_crackers + 1000)

# 加分习题：
'''
加分习题
1. 倒着将脚本读完，在每一行上面添加一行注解，说明这行的作用。
2. 从最后一行开始，倒着阅读每一行，读出所有的重要字符来。
3. 自己编至少一个函数出来，然后用10种方法运行这个函数。
'''