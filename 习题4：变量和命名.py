cars = 100
sapce_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars- drivers
cars_driven = drivers
carpool_capacity = cars_driven * sapce_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# 加分习题
# 1.在程序中使用4.0作为space_in_a_car的值，这样做有必要吗？如果只用4会有什么问题
# 这里会影响到cars_not_driven的类型，4.0下是浮点数，输出为120.0
# 而4下是整数，输出为120

# 2.记住“4.0”是一个浮点数，自己研究一下这是什么意思。

# 3.在每一个变量赋值的上一行加上一行注释

# 4.记住 = 的名字是等于（equal），它的作用是为东西取名字

# 5.记住 _ 是下划线字符

# 6.将Python作为计算器运行起来，不过这一次在计算过程中使用变量名来做计算
# 常见的变量名有i,x,y等等