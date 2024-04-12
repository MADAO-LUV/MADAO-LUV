"""
有 N种物品和一个容量是 V的背包，每种物品都有无限件可用。(与01背包不同，01背包里面的物品只能用1次，而这里可以用无限次)
第 i种物品的体积是 vi,价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N行，每行两个整数 vi,wi，用空格隔开，分别表示第 i种物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

即使进行了记忆化搜索 但是还是超时了 ，所以进行进一步优化 dp以及(roll array)滚动数组实现
"""
n,m = map(int,input().split()) #n表示物品个数 m表示可以容纳的体积
N = 1010
v = [0 for i in range(N)] #表示体积
w = [0 for i in range(N)] #表示价值
#f = [[0]*N for i in range(N)]  #正序dp 或者倒序 dp 所需要的
f = [0 for i in range(N)] #一维数组
for i in range(1,n+1):
    v[i],w[i] = map(int,input().split())
#
#正序dp 滚动数组 优化空间
"""
01背包问题倒序的目的就是 只让每个物品最多拿一次
01背包如果正序枚举举体积的话，就会让物品被拿多次，从而违法规则
但是完全背包不用考虑这个问题，因为本身就是可以拿多次的!所以完全背包可以正序枚举体积
"""
for i in range(1,n+1):
    for j in range(v[i],m+1):
          f[j] = max(f[j],f[j-v[i]]+w[i])
print(f[m])

"""
倒序dp
for i in range(n,0,-1):
    for j in range(0,m+1):
        if j < v[i]:
            f[i][j] = f[i+1][j]
        else:
            f[i][j] = max(f[i+1][j],f[i][j-v[i]]+w[i])
print(f[1][m])

正序dp
for i in range(1,n+1):
    for j in range(0,m+1):
        if j < v[i]:
            f[i][j] = f[i-1][j]
        else:
            f[i][j] = max(f[i-1][j],f[i][j-v[i]]+w[i])
print(f[n][m])
"""