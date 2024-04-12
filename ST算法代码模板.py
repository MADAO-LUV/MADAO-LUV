"""
ST算法模板
例如，有10个元素a[1..10] = {5,3,7,2,12,1,6,4,8,15},创建查询最大值的ST表。
F[i,j]表示[i,i+2**j-1]区间的最值，区间长度为2**j
"""
from math import *
n,m = map(int,input().split()) #
a = [0] + list(map(int,input().split()))
k = int(log2(n)) #获取最大区间值
dp = [[0 for col in range(k+1)] for row in range(n+1)]

def st_init():
    global dp
    for i in range(1,n+1): dp[i][0]=a[i]
    p=int(log2(n))
    for k in range(1,p+1):
        for s in range(1,n+2-(1<<k)):
            dp[s][k]=min(dp[s][k-1],dp[s+(1<<(k-1))][k-1])

def st_query(i):
    k=int(log2(m))
    return min(dp[i][k],dp[i+m-(1<<k)][k])

st_init()
for i in range(1,n+2-m):
    print(st_query(i))