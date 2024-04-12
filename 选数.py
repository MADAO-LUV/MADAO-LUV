"""
已知n个整数x1,x2,x3....Xn.以及1个整数k(k<n),从n个整数中任选
k个整数相加,可分别得到一系列的和，例如当n=4,k=3,4个整数分别为
3,7,12,19时，可得全部的组合和它们的和
"""
n,k = map(int,input().split())
q = [0] + list(map(int,input().split(',')))
arr = [0 for i in range(n+1)] #用来暂时存放数字
res = 0

def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)):
        if x % i == 0:
            return False
    return True

#x 记录当前枚举到哪个位置 start 记录当前位置从几开始枚举
def DFS(x,start):
    global res
#减枝操作,这里说明它填不满k个数
#x-1是表达的是已经被选了数 n-start+1得出还有几个数没选
    if (x - 1 + n - start + 1) < k:
        return #直接retrun掉


    #因为选择了k个数
    if x > k:
        sum = 0
        for j in range(1,k+1):
            sum += arr[j]
        if is_prime(sum):
            res += 1
        print(sum)
        return

#从start处开始枚举
    for i in range(start,n+1):
        arr[x] = q[i]
        DFS(x+1,i+1)
        arr[x] = 0 #回溯

DFS(1,1)
print(res)