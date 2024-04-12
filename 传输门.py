"""
在一个神奇空间里有N个房间，房间从1到N编号，每个房间可能有一个或多个传送门
，每个传送门都有一个编号，如果相同编号的传送门同时出现在多个房间中，表示这些房间可以互通

给定两个房间的编号A和B，请找出从房间A到达B最少需要经过几个传送门。
例如:N=3,3个房间中传送门的编号分别为:
房间1:1,4,6
房间2:2,3,4,8
房间3:3，6，9
"""
n = int(input()) #房间数量
a = []#二维列表
for x in range(n):
    a.append(input().split(','))
x,y = list(map(int,input().split(',')))
x,y = x-1,y-1 #房间编号一致 与二维列表中的实际编号匹配
visited = [] #标记已经访问过的房间
res = [] #到达目标房间的传递门数量 ,min
#DFS 深度优先搜素
def find(room,cnt):
    if room == y:
        res.append(cnt) #传送门的数量
        return
    visited.append(room)
    for i in range(len(a)):
        if i not in visited and set(a[room]) & set(a[i]): # 当前房间编号不在visited里，以及room与当前房间编号有交集,共同传送门
            find(i,cnt+1)
    visited.pop()#回溯

find(x,0)
if len(res) == 0:
    print(-1) #没有传送门的时候的情况
else:
    print(min(res))