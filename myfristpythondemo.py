counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1


print(a)
print(b)
print(c)


a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)

a, b, c, d = 20, 5.5, True, 4 + 3j

#Number（数字）
#Python3 支持 int、float、bool、complex（复数）。

#a,b,c,d=20,5.5,True,4+3j
#print((type(a),type(b),type(c),type(d))
str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串


print('Ru\noob') #换行输出
print(r'Ru\noob')#如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串


word = 'Python'
print(word[0], word[5])#P n
print(word[-1], word[-2]) # n o

#1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义.
# 字符串可以用+运算符连接在一起，用*运算符重复。
#3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
#4、Python中的字符串不能改变。


#List（列表）
#List（列表） 是 Python 中使用最频繁的数据类型。

#列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

#与Python字符串不一样的是，列表中的元素是可以改变的：
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []   # 将对应的元素值设置为 []
print(a)

#Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
letters=['c','h','e','c,','k','i','o']
letters=letters[1:4:2]

print(letters)

#Tuple（元组）
#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

#元组中的元素类型也可以不相同：
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

tup1 = (1, 2, 3, 4, 5, 6)
print(tup1[0])

import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

#set
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

#字典
dict={}
print("dict=",dict)
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

#Python 条件语句
flag=False
name='luren'
if name=='python':
    flag=True
    print  ('welcome boss')
else:
    print  (name)

# 例2：elif用法

num = 5
if num == 3:  # 判断num的值
    print( 'boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print( 'roadman')
     # 条件均不成立时输出

#由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
# 例3：if语句多个条件

num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print  ('hello')
# 输出结果: hello

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print( 'undefine1')




