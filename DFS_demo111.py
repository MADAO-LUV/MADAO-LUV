"""
动态规划 --->逆序 或者 正序 写
"""
n,m = map(int,input().split())
N = 1010
v = [0 for i in range(N)]
w = [0 for i in range(N)]
f = [0 for i in range(N)]
for i in range(n):
    v[i],w[i] = map(int,input().split())

for i in range(1,n+1):
    for j in range(m,0,-1):
        f[j] = max(f[j],f[j-v[i]]+w[i])
print(f[m])











