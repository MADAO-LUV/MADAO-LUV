"""
有 N件物品和一个容量是 V的背包，背包能承受的最大重量是 M
每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi
。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。

输入格式
第一行三个整数，N,V,M
，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。

接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i件物品的体积、重量和价值。

输出格式
输出一个整数，表示最大价值。

这是已经进行了记忆化搜索优化的 ，但是再acwing中仍然超时，所以进行倒序dp优化
"""
N,V,M = map(int,input().split()) #N件物品,背包容量为V 背包最大承重为M
v = [0 for i in range(1010)] #容量
m = [0 for i in range(1010)] #重量
w = [0 for i in range(1010)] #价值
memo = [[[0]*110  for i in range(110)] for i in range(1010)] #开三维数组 memo[x][spv][spm]
for i in range(1,N+1):
    v[i],m[i],w[i] = map(int,input().split())

#暴力dfs x表示当前为第x个物品 spv 表示剩余的容量 spm表示剩余承重
def dfs(x,spv,spm):
    if memo[x][spv][spm]:
        return memo[x][spv][spm]
    if x > N:
        res = 0
    else:
        if spv >= v[x] and spm >= m[x]:
            res = max(dfs(x+1,spv,spm),dfs(x+1,spv-v[x],spm-m[x])+w[x])
        else:
            res = dfs(x+1,spv,spm)
    memo[x][spv][spm] = res
    return res
print(dfs(1,V,M))
