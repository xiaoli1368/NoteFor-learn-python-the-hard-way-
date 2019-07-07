print("Let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do \n newlines and \t tabs")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars /100
    return(jelly_beans, jars, crates)

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))

# 加分习题
'''
1. 记得仔细检查结果,从后往前倒着检查,把代码朗读出来,在不清楚的位置加上注释。
2. 故意把代码改错,运行并检查会发生什么样的错误,并且确认你有能力改正这些错误。
'''