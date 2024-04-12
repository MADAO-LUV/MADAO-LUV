"""




"""
m,n = input().split(',')
m,n = int(m),int(n)
a = []
for x in range(m):
    tmp = input().split(',')
    a.append(tmp)

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(x,y):
    if x < 0 or x > m or y < 0 or y > n: #越界
        return
    if a[x][y] == "X": #周边是杂草的情况
        return
    #R--->x
    a[x][y] = "X"
    for dx,dy in dirs: #四个方向检测
        nx,ny = x+dx,y+dy
        dfs(nx,ny)


cnt = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == "R":
            dfs(i,j) #深度优先收索
            cnt += 1
print(cnt)