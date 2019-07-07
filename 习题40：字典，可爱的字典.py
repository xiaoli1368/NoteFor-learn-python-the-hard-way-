# --------------------------
things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

# ---------------------------
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "San Francisco"
print(stuff['city'])

# ---------------------------
stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
print(stuff)

# ---------------------------
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

# ---------------------------
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return(themap[state])
    else:
        return("Not found.")

# ok pay attention!
cities['_find'] = find_city # 把函数放到了字典里

while True:
    print("State? (ENTER to quit)")
    state = input("> ")

    if not state: break # 这里直接回车则 input 接受到的为空或者0， not state 为 True

    # this line is the most important ever! study!
    city_found  = cities['_find'](cities, state) # 用字典中的函数来寻找 state
    print(city_found)

# 加分习题
'''
1. 在 Python 文档中找到 dictionary (又被称作 dicts, dict) 的相关的内容，学着对 dict做更多的操作。
2. 找出一些 dict 无法做到的事情。例如比较重要的一个就是 dict 的内容是无序的，你可以检查一下看看是否真是这样。
3. 试着把 for-loop 执行到 dict 上面，然后试着在 for-loop 中使用 dict 的 items() 函数，看看会有什么样的结果。
'''

# 这个挺重要的