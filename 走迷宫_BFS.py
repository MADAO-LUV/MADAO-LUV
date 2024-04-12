"""
给定一个n * m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路
1表示不可以通过的墙壁。
最初，有一个人位于左上角(1,1)处,已知该人每次可以向上，下，左，右任意一个方向移动一个位置
请问，该人从左上角移动到右下角(n,m)处的数字为0，且一定至少存在一条通路

输入格式:
第一行包含两个整数n和m
接下来n行，每行包含m个整数(0或1)，表示完整的二维数组迷宫
输出格式:
输出一个整数，表示从左上角移动至右下角的最少移动次数.

BFS可以解决的2类问题
1.从A出发是否存在到达B的路径:DFS BFS
2.从A出发到达B的最短路径:数据小20以内的话，DFS也不是不可以
"""
from queue import Queue
mp = []
for i in range(0,30):
    mp.append(input())
for i in range(len(mp)):
    mp[i] = '1' + mp[i] + '1'
mp = [52 * '1'] + mp + [52 * '1']
vis = [list(map(int,list(i))) for i in mp]
k = ('D','L','R','U')
dir = ((1,0),(0,-1),(0,1),(-1,0)) #将方向都定义为元组，不可以更改
#下面是bfs
vis[1][1] = 1
q = Queue()
q.put((1,1," "))
while q.qsize() != 0:
    now = q.get()
    if now[0] == 30 or now[1] == 50:
        print(now[2])
        exit
    for i in range(4):
        x = now[0] + dir[i][0]
        y = now[1] + dir[i][1]
        if vis[x][y] != 1:
            vis[x][y] = 1
            path = now[2] + k[i]
            q.put((x,y,path))