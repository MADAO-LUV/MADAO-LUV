n,m = map(int,input().split())
N = 1010
v = [0 for i in range(N)]
w = [0 for i in range(N)]
f = [0 for i in range(N)]
for i in range(1,n+1):
    v[i],w[i] = map(int,input().split())

for i in range(1,n+1):
    for j in range(m,-1,-1):
        if j >= v[i]:   #那么就是类似于c里面写的 for (int j = m; j >= w[i]; j--): 进行枚举判断
            f[j] = max(f[j],f[j-v[i]]+w[i])

print(f[m])