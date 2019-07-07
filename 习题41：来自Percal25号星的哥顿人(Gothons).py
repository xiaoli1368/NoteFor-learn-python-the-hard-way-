# rom sys import exit这行就是把sys模块中的exit函数引用进来，这样就覆盖了默认的exit()，
# 其实这个默认的exit()是site.Quitter，site是一个在大多情况下会被自动import的库。
# 简单说说这两者的区别，sys.exit()是一个比较纯粹的程序退出函数，通过抛出SystemExit(status)来使得进程退出，在一般的python代码中应当使用它：
# exit()是被设计成在交互式Interpreter时方便用户使用的一个辅助类，不应当在正式程序中使用。
# 它的好处就是提供用户友好性，一个简单的例子：
# 链接：https://www.zhihu.com/question/33591121/answer/57219214

from sys import exit # 导入模组中的exit函数
from random import randint # 导入模组-产生伪随机数

def death():
    # 定义死亡函数
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    print(quips[randint(0, len(quips)-1)])
    exit(1)
# 不同函数之间隔一行

def central_corridor():
    # 定义中间走廊
    print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
    print("your entire crew. You are the last surviving member and your last")
    print("mission is to get the neutron destruct bomb from the Weapons Armory,")
    print("put it in the bridge, and blow the ship up after getting into an ")
    print("escape pod.")
    print("\n")
    print("You're running down the central corridor to the Weapons Armory when")
    print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
    print("flowing around his hate filled body. He's blocking the door to the")
    print("Armory and about to pull a weapon to blast you.")
    
    action = input("> ")

    if action == "shoot!":
        print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
        print("His clown costume is flowing and moving around his body, which throws")
        print("off your aim. Your laser hits his costume but misses him entirely. This")
        print("completely ruins his brand new costume his mother bought him, which")
        print("makes him fly into an insane rage and blast you repeatedly in the face until")
        print("you are dead. Then he eats you.")
        return('death')

    elif action == "dodge!":
        print("Like a world class boxer you dodge, weave, slip and slide right")
        print("as the Gothon's blaster cranks a laser past your head.")
        print("In the middle of your artful dodge your foot slips and you")
        print("bang your head on the metal wall and pass out.")
        print("You wake up shortly after only to die as the Gothon stomps on")
        print("your head and eats you.")
        return('death')
    
    elif action == "tell a joke":
        print("Lucky for you they made you learn Gothon insults in the academy.")
        print("You tell the one Gothon joke you know:")
        print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
        print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
        print("While he's laughing you run up and shoot him square in the head")
        print("putting him down, then jump through the Weapon Armory door.")
        return('laser_weapon_armory')

    else:
        print("DOES NOT COMPUTE!")
        return('central_corridor')

def laser_weapon_armory():
    # 激光武器军械库
    print("You do a dive roll into the Weapon Armory, crouch and scan the room")
    print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
    print("You stand up and run to the far side of the room and find the")
    print("neutron bomb in its container. There's a keypad lock on the box")
    print("and you need the code to get the bomb out. If you get the code")
    print("wrong 10 times then the lock closes forever and you can't")
    print("get the bomb. The code is 3 digits.")

    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) # 钥匙是随机的三个数
    guess = input("[keypad]> ")
    guesses = 0

    while guess != code and guesses < 10: # 当碰巧答对密码或者尝试了11此后跳出循环
        print("BZZZZEDDD!")
        guesses += 1
        guess = input("[keypad]> ")

    if guess == code:
        print("The container clicks open and the seal breaks, letting gas out.")
        print("You grab the neutron bomb and run as fast as you can to the")
        print("bridge where you must place it in the right spot.")
        return('the_bridge')
    else:
        print("The lock buzzes one last time and then you hear a sickening")
        print("melting sound as the mechanism is fused together.")
        print("You decide to sit there, and finally the Gothons blow up the")
        print("ship from their ship and you die.")
        return('death')

def the_bridge():
    # 桥
    print("You burst onto the Bridge with the neutron destruct bomb")
    print("under your arm and surprise 5 Gothons who are trying to")
    print("take control of the ship. Each of them has an even uglier")
    print("clown costume than the last. They haven't pulled their")
    print("weapons out yet, as they see the active bomb under your")
    print("arm and don't want to set it off.")

    action = input("> ")

    if action == "throw the bomb": # 扔掉炸弹
        print("In a panic you throw the bomb at the group of Gothons")
        print("and make a leap for the door. Right as you drop it a")
        print("Gothon shoots you right in the back killing you.")
        print("As you die you see another Gothon frantically try to disarm")
        print("the bomb. You die knowing they will probably blow up when")
        print("it goes off.")
        return('death')

    elif action == "slowly place the bomb": # 慢慢放下炸弹
        print("You point your blaster at the bomb under your arm")
        print("and the Gothons put their hands up and start to sweat.")
        print("You inch backward to the door, open it, and then carefully")
        print("place the bomb on the floor, pointing your blaster at it.")
        print("You then jump back through the door, punch the close button")
        print("and blast the lock so the Gothons can't get out.")
        print("Now that the bomb is placed you run to the escape pod to")
        print("get off this tin can.")
        return('escape_pod')
    else:
        print("DOES NOT COMPUTE!")
        return("the_bridge")

def escape_pod(): # 逃离豆荚？
    print("You rush through the ship desperately trying to make it to")
    print("the escape pod before the whole ship explodes. It seems like")
    print("hardly any Gothons are on the ship, so your run is clear of")
    print("interference. You get to the chamber with the escape pods, and")
    print("now need to pick one to take. Some of them could be damaged")
    print("but you don't have time to look. There's 5 pods, which one")
    print("do you take?")

    good_pod = randint(1,5)
    guess = input("[pod #]> ")

    if int(guess) != good_pod:
        print("You jump into pod %s and hit the eject button." % guess)
        print("The pod escapes out into the void of space, then")
        print("implodes as the hull ruptures, crushing your body")
        print("into jam jelly.")
        return('death')
    else:
        print("You jump into pod %s and hit the eject button." % guess)
        print("The pod easily slides out into space heading to")
        print("the planet below. As it flies to the planet, you look")
        print("back and see your ship implode then explode like a")
        print("bright star, taking out the Gothon ship at the same")
        print("time. You won!")
        exit(0)

ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod
} # 这是一个字典，不同入口对应不同的函数

def runner(map, start): 
    # 主函数
    next = start

    while True:
        room = map[next]
        print("\n--------")
        next = room()

runner(ROOMS, 'central_corridor')

# 加分习题
'''
1. 解释一下返回至下一个房间的工作原理。
2. 创建更多的房间，让游戏规模变大。
3. 除了让每个函数打印自己以外，再学习一下“文档字符串 (doc strings)”式的注解。
   看看你能不能将房间描述写成文档注解，然后修改运行它的代码，让它把文档注解
   打印出来。
4. 一旦你用了文档注解作为房间描述，你还需要让这个函数打印出用户提示吗？试着
   让运行函数的代码打出用户提示来，然后将用户输入传递到各个函数。你的函数应
   该只是一些 if 语句组合，将结果打印出来，并且返回下一个房间。
5. 这其实是一个小版本的“有限状态机 (finite state machine)”，找资料阅读了解一下，
   虽然你可能看不懂，但还是找来看看吧。
6. 我的代码里有一个 bug，为什么门锁要猜测 11 次？
'''