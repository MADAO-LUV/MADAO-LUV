"""
有N件物品和一个容量是V的背包，每件物品只能使用依次，
第i件物品的体积vi，其价值是wi

求解将那些物品装入背包，可使这些物品的总体积不超过背包容量
且总价值最大
动态规划是全局最优解
"""
n,m = map(int,input().split())
N = 1010
v = [0 for i in range(N)]
w = [0 for i in range(N)]
#记忆化搜索的mem 数组 的定义: 从第x个物品开始,x-n的物品最大总价值[x,n],总体积<=j的最大价值 倒序推
#正序递推 memo[i][j] 从前i个物品[1,i]中选，选总体积 <= j 的物品的总价值的最大值
memo = [[0]*N for i in range(N)]

def dfs(x,sp):
    if memo[x][sp]:
        return memo[x][sp]
    cnt = 0
    if x > n:
        cnt = 0
    elif sp < v[x]:
        cnt = dfs(x+1,sp)
    else:
        cnt = max(dfs(x+1,sp),dfs(x+1,sp-v[x])+w[x])
    memo[x][sp] = cnt
    return cnt
for i in range(1,n+1):
    v[i],w[i] = map(int,input().split())
a = dfs(1,m)
print(a)
