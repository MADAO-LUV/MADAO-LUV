""""
洛谷 p1746
"""
from queue import Queue

n = eval(input())
mp = []
for i in range(n):
    mp.append(input())
for i in range(len(mp)):
    mp[i] = '1' + mp[i] + '1'
mp = [(n + 2) * '1'] + mp + [(n + 2) * '1']
vis = [list(map(int, list(i))) for i in mp]
# 基本模板，为这个迷宫外层加了一层围墙
# 使得我们的起始点和终点与输入的一一对应
dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
x1,y1,x2,y2 = map(int,input().split())
# 以下是bfs
vis[x1][y1] = 1
q = Queue()  # 开始进行bfs
path = 0
# 以下是bfs
def bfs(x1,y1):
    dist = [[-1]*(n+2) for i in range(n+2)]
    q.put((x1,y1))
    dist[x1][y1] = 0

    while q.qsize() != 0:
        now = q.get()
        for i in range(4):
            x = now[0] + dirs[i][0]
            y = now[1] + dirs[i][1]

            if x < 1 or x > n or y < 1 or y > n:
                continue
            if mp[x][y] == '1':
                continue
            if dist[x][y] >= 0:
                continue
            q.put((x,y))
            dist[x][y] = dist[now[0]][now[1]] + 1

            if dist[x2][y2] > 0:
                return dist[x2][y2]
    return -1

res = bfs(x1,y1)
print(res)



