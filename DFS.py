"""
深度优先 --- Depth First Search 树/图
1.矩阵最长递减路径：
    1.递归解法
    2.中间解保存
"""
lst = [
    [1,1,3],
    [2,3,4],
    [1,0,1]
]
m,n = 3,3 #行 列
#i 为x  j为y
def dfs(i,j,val):
    if i < 0 or i == m:
        return 0 #行越界
    if j < 0 or j == n:
        return 0 #列越界
    if lst[i][j] >= val:
        return 0 #当前的i，j大于val时，不满足
    res = 1 #表示自己的那个点
    res = max(res,1 + dfs(i-1,j,lst[i][j])) #向上
    #lst[i][j]为当前的值，与上面的值进行比较，如果满足就上走
    res = max(res, 1 + dfs(i + 1, j, lst[i][j]))
    res = max(res, 1 + dfs(i, j - 1, lst[i][j]))
    res = max(res, 1 + dfs(i, j + 1, lst[i][j]))

    return res

for x in range(m):
    for y in range(n):
        res = dfs(x,y,100) #100 为初始值，让dfs启动，一定要比这里的所有值大
        print(res,end=" ")
    print()