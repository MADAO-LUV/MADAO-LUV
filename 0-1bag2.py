
def ks(n,C):
    if memo[n][C] != 0:
        for row in memo:
            print(row)
        print()
        return memo[n][C] #取出结果
    if n == 0 or C == 0:
        result = 0
    elif w[n] > C:
        result = ks(n-1,C)
    else:
        tmp1 = ks(n-1,C)
        tmp2 = v[n] + ks(n-1,C-w[n])
        result = max(tmp1,tmp2)
    memo[n][C] = result #存储结果
    return result

#n = 5;C = 10
n,C = list(map(int,input().split()))
w = [0]; v=[0]
for x in range(n):
    w1,v1 = list(map(int,input().split()))
    w.append(w1)
    v.append(v1)


memo = [[0] * (C+1) for i in range(n+1)] #将数据存储在列表中
res = ks(n,C)
print(res)