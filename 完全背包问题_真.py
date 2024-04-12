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
memo = [[0]*N for i in range(N)]  #进行记忆化优化

for i in range(1,n+1):
    v[i],w[i] = map(int,input().split())
#进行记忆化优化
def dfs(x,spv):
    if memo[x][spv]:
        return memo[x][spv]
    res = 0
    if x > n:
        return 0
    else:
        if spv < v[x]:
            res = dfs(x+1,spv)
        else:
            res = max(dfs(x+1,spv),dfs(x,spv-v[x])+w[x])#这里的dfs(x,spv-v[x])+w[x]表示重复利用物品x 因为完全背包可以重复使用物品
    memo[x][spv] = res
    return res
print(dfs(1,m))
