"""
从1~n这n个整数中随机选取任意多个，输出所有可能的选择方案
"""
"""
递归/DFS 最重要的是 顺序，不重复，不漏解
顺序:从1-n依次考虑每个数 选/不选
"""
from math import *
st = [0 for i in range(20)] #记录每个数的转台 0表示还没考虑 1表示选 2表示不选
n = eval(input())

#x表示当前枚举到了哪个位置
def DFS(x):
    if x > len(str(n)):
        for i in range(1,len(str(n))+1):
            if st[i] == 1:
                print(i,end = " ")
        print("\n")
        return  #什么都不返回

    #选
    st[x] = 1
    DFS(x+1)
    st[x] = 0 #回溯

    #不选
    st[x] = 2
    DFS(x+1)
    st[x] = 0 #恢复现场

DFS(1)