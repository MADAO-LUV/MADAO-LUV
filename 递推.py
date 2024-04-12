"""
mem = [0 for x in range(int(1e5))]
def dfs(num):
    if mem[num]:
        return mem[num]
    cnt = 0
    if num == 1:
        cnt = 1
    elif num == 2:
        cnt = 2
    else:
        cnt = dfs(num-1) + dfs(num-2)
    mem[num] = cnt
    return cnt
"""
"""
记忆化搜索省去很多的分支

递归的过程：“归”的过程才是产生答案的过程
“递”的过程是 分解子问题的过程

“递” --> 自顶向下
"归" --> 自下向上 （递归搜素数的底） 已知最小问题的答案
"""
f = [0 for i in range(int(1e5))]
n = eval(input())
f[1],f[2] = 1,2
if (n == 1 or n == 2):
    print(f[n])
    exit()
"""
#动态规划：
用来优化空间的    
newp,tmp1,tmp2 = 0,1,2
for i in range(3,n+1):
    newp = tmp1 + tmp2
    tmp1 = tmp2
    tmp2 = newp
print(newp)
"""
for i in range(3,n+1):
    f[i] = f[i-1] + f[i-2]
print(f[n])

"""
优化时间 ---> 拿空间换时间
最简单的dp ---> 递推
记忆化搜索 = 暴力dfs + 记录答案
递推的公式 = dfs 向下递归的公式
递归数组的初始值 = 递归的边界
"""