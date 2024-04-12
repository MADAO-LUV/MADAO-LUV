"""
01背包问题，状态转移

"""
n,m = map(int,input().split())
N = 1010
v = [0 for i in range(N)]
w = [0 for i in range(N)]
for i in range(1,n+1):
    v[i],w[i] = map(int,input().split())
f = [[0]*N for i in range(N)]
#记忆化搜索memo 的定义从第x个物品开始(x-n),总体积<=j的最大价值，倒序搜索 后x个
#从(1-x)个 x个
#从下往上推
for i in range(n,0,-1):
    for j in range(0,m+1):
        if j < v[i]:
            f[i][j] = f[i+1][j]
        elif j >= v[i]: #选装入 或者不装
#f[i][j]代表从第i个到结尾物品中，选取的不超过体积j的最大价值

            f[i][j] = max(f[i+1][j],f[i+1][j-v[i]]+w[i])
print(f[1][m])

"""
for i in range(1,n+1):
    for j in range(0,m+1):
        if j < v[i]:
            f[i][j] = f[i-1][j]
        elif j >= v[i]:
            f[i][j] = max(f[i-1][j],f[i-1][j-v[i]]+w[i])
print(f[n][m])
"""
