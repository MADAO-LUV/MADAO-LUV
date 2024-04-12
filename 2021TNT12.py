"""
1.不对文件读操作的是:readtext()
readline() readlines() read()这三格都是读取操作

f = open("data.txt") 打开文件
f.close()关闭文件

a.read()读取全部内容
b. readlines 把不空的每一行读取（一行行读取），每行放到列表里面
c.readline 读取当前的一行数据，每次读一行



random,uniform(a,b) 随机生成a,b的浮点数

d.keys() ---取字典的键， d.values() ---取字典的值


对于turtle
goto(x,y) --- 让海龟跑到对应的点
pensize() --- 设置海龟画笔的大小
setup()  --- 定义窗体的大小和相对位置

a = 3 + 2j "j"或者"J"都可以
#real 是实部  image 是虚部
a.real --- 指的是a的实数部分
a.image --- 指的是a的虚数部分

sorted()排序后返回list
c = [1:"one",3:"three",2:"two"]
sorted(c) ---> [1,2,3]
sorted(c.values) ---> ['one','two','three']












"""