from sys import argv
from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" % (from_file, to_file))

# we could do thess two on one line, how?
input_cac = open(from_file)
indata = input_cac.read()
# 可以写成这样：indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

output_cac = open(to_file, 'w')
output_cac.write(indata)

print("Alright, all done.")

output_cac.close()
input_cac.close()

# 命令行下使用 type 读取txt文件

# 总结：
'''
在我们调用open()时，我们输入了两个参数，第一个是要打开文件的名称，第二个是'w'。
这里，第二个参数其实是在告诉Python我们要以写入模式打开这个文件，当然还有其他的文件打开模式。
'r'读取模式
'a'附加模式（既给文件附加内容而不是覆盖内容）
'r+'读取和写入模式
默认情况下，Python将以只读模式打开文件
'''

# 加分习题
'''
1. 再多读读和 import 相关的材料，将 python 运行起来，试试这一条命令。试着看看自己能不能摸出点门道，当然了，即使弄不明白也没关系。
2. 这个脚本 实在是 有点烦人。没必要在拷贝之前问一遍把，没必要在屏幕上输出那么多东西。试着删掉脚本的一些功能，让它使用起来更加友好。
3. 看看你能把这个脚本改多短，我可以把它写成一行。
4. 我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接(con*cat*enate)”到一起，不过实际上它最大的用途是打印文件内容到屏幕上。
   你可以通过 man cat 命令了解到更多信息。
5. 使用 Windows 的同学，你们可以给自己找一个 cat 的替代品。关于 man 的东西就别想太多了，Windows 下没这个命令。
6. 找出为什么你需要在代码中写 output.close() 。
'''