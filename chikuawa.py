n = eval(input())


def dfs(x):
    cnt = 0
    if x < 0:
        return 1
    for i in range(1,x):
        cnt = max(cnt,max(i*(x-i),dfs(x-i)*i))
    return cnt
print(dfs(n))
