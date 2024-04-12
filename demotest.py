"""
已知n个整数x1,x2,x3....Xn.以及1个整数k(k<n),从n个整数中任选
k个整数相加,可分别得到一系列的和，例如当n=4,k=3,4个整数分别为
3,7,12,19时，可得全部的组合和它们的和
"""
n,k = map(int,input().split(','))
q = [0] + list(map(int,input().split(',')))
arr = [0 for i in range(n+2)]
res = 0

def is_Prime(j):
    if j < 2:
        return False
    for i in range(2,int(j**0.5)):
        if j % i == 0:
            return False
    return True

def dfs(x,start):
    global res
    if (x + n - start) < k:
        return

    if x > k:
        cnt = 0
        for j in range(1,k+1):
            cnt += arr[j]
        if is_Prime((cnt)):
                res += 1
        print(cnt)
        return

    for i in range(start,n+1):
        arr[x] = q[i]
        dfs(x+1,i+1)
        arr[x] = 0
dfs(1,1)
print(res)