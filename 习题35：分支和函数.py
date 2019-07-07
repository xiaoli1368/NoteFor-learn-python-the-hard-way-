from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next: # 也就是说输入的数字中必须有 0 或者 1
        how_much = int(next)
    else:
        dead ("Man, learn to type a number.")
    
    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit (0)
    else:
        dead ("You greedy bastard!") # 你这贪婪的混蛋

def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.") # 熊有一堆蜂蜜
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        next = input("> ")
        
        if next == "take honey":
            dead ("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved: # 嘲讽熊
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead ("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")

def cthuhu_room():
    print ("Here you see the great evil Cthulhu.") # 邪恶的克苏鲁
    print ("He, it, whatever stares at you and you go insane.") # 他，无论什么盯着你，你都疯了
    print ("Do you flee for your life or eat your head?") # 你是逃命还是吃头？
    
    next = input("> ")
    
    if "flee" in next:
        start() # 这里重新回到开始的地方
    elif "head" in next:
        dead ("Well that was tasty!")
    else:
        cthuhu_room()

def dead(why):
    print (why, "Good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")
    
    next = input("> ")
    
    if next == "left":
        bear_room() # 熊房间
    elif next == "right":
        cthuhu_room() # 邪神房间
    else:
        dead ("You stumble around the room until you starve.")
        # 你在房间里绊倒直到你饿死（这也太恶毒了吧）
       
start()

# 这游戏挺有意思的啊

# 加分习题
'''
1.把这个游戏的地图画出来，把自己的路线也画出来。
2.改正你所有的错误，包括拼写错误。
3.为你不懂的函数写注解。记得文档注解该怎么写吗？
4.为游戏添加更多元素。通过怎样的方式可以简化并且扩展游戏的功能呢？
5.这个 gold_room 游戏使用了奇怪的方式让你键入一个数字。这种方式会导致什么样的 bug？
  你可以用比检查 0、1 更好的方式判断输入是否是数字吗？int() 这个函数可以给你一些头绪。
'''