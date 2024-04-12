lst = [
    [1,1,1,0,0,0,0],
    [1,1,0,1,0,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,1,1,1]
]

m = len(lst) #有多少行二维列表
n = len(lst[0]) #有多少列
"""
不等于1的情况有两个：1.被标记好的情况 2.为海域的0
"""
def mark_current_island(x,y): #mark标记1-2
    if x<0 or x>m-1 or y>n-1 or lst[x][y] != 1:
        return 0
    lst[x][y] = 2#标记为2
    mark_current_island(x-1,y) #向上
    mark_current_island(x+1,y)#先下
    mark_current_island(x,y-1)#向左
    mark_current_island(x,y+1)#向右


cnt = 0#计算器
for i in range(m):
    for j in range(n):
        if lst[i][j] == 1:
            mark_current_island(i,j)
            cnt += 1
print(cnt)
#把整个标记情况打印出来
for row in lst:
    print(row)