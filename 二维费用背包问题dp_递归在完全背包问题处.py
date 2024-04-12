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

倒序dp实现 模拟”归“操作

正序dp实现 就是分别改变 i为正序遍历
并且i+1 变为 i-1
f[N][V][M]
"""
N,V,M = map(int,input().split()) #N件物品,背包容量为V 背包最大承重为M
v = [0 for i in range(1010)] #容量
m = [0 for i in range(1010)] #重量
w = [0 for i in range(1010)] #价值
f = [[[0]*110  for i in range(110)] for i in range(1010)] #开三维数组 f[x][spv][spm]
for i in range(1,N+1):
    v[i],m[i],w[i] = map(int,input().split())

for i in range(N,0,-1):
    for j in range(0,V+1):
        for k in range(0,M+1):
            if j < v[i] or k < m[i]:
                f[i][j][k] = f[i+1][j][k]
            else:
                f[i][j][k] = max(f[i+1][j][k],f[i+1][j-v[i]][k-m[i]]+w[i])
print(f[1][V][M])