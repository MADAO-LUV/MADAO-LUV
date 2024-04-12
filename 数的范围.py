"""
给定一个按照升序排列的长度为n的整数数组，以及q个查询
对于每个查询，返回一个元素k的起始位置和终止位置(位置从0开始计数)
如果数组中不存在该元素，则返回 -1 -1

输入格式:
第一行包含整数n和q，表示数组长度和询问个数
第二行包含n个整数(均在1~10000范围内)，表示完整数组
接下来q行，每行包含一个整数k，表示一个询问元素
"""
n,q = map(int,input().split()) #6个数 3次询问
lst = list(map(int,input().split())) + [0]
N = 10010 #根据题目中n的范围来确定数组应该开多大，开的范围必须要比n大一点
#数组中的数是num，被询问数是x
def isBule(num,x):  #因为我们知道isBule有什么用了，就可以在下一次的优化中删除，用里面的条件代替
    if num < x:
        return True
    else:
        return False
#第二个二分查找找的是:被询问数的最后一次出现的位置(下标)
def isBule2(num,x):
    if num <= x:
        return True
    else:
        return False


def binary_Search(n,tmp1):
    l,r = -1,n
    while (l+1 < r):
        mid = (l+r) >> 1 #与 (l+r)//2效果相同
        if isBule(lst[mid],tmp1):
            l = mid
        else:
            r = mid
    if lst[r] == tmp1:
        return r
    else:
        return -1

def binary_Search2(n,tmp2):
    l,r = -1,n
    while (l+r < r):
        mid = (l+r) >> 1
        if isBule2(lst[mid],tmp2):
            l = mid
        else:
            r = mid
    if lst[l] == tmp2:
        return l
    else:
        return -1

for i in range(q):
    tmp1 = eval(input())
    res1 = binary_Search(n,tmp1)
    res2 = binary_Search2(n,tmp1)
    print(res1,res2,end = " ")

