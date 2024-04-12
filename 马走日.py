"""
马走日
二维坐标表示：
1.第一象限：(2,1) , (1,2)
2.第二象限: (-2,1) , (-1,2)
3.第三象限:(-2,-1), (-1,-2)
4.第四象限：(2,-1),(1,-2)

快速生成二维列表
假设我有m,n
[[0]*n for i in range(m)] 表示m行，n列
取值范围:(0 ---m-1)  (0 ---n-1)
"""
t = int(input())
for _ in range(t):
    m,n,a,b = map(int,input().split())


borad = [[0]*n for i in range(m)] #用0标记没有走过的地方
dirs = [(2,1),(1,2),
        (-2,1),(-1,2),
        (-2,-1),(-1,-2),
        (2,-1),(1,-2)
        ]
cnt = 0 #计数器 不能
def move(x,y,step):
    global cnt
    print(x,y,step)
    if step == m*n:
        cnt += 1
        print("-----------------")
        return
    #dirs[i] #表示取那个元组
    for i in range(8):
        next_x = dirs[i][0] + x #行的偏移量
        next_y = dirs[i][1] + y#列的偏移量
        if next_x >= 0 and next_x <= m-1 and next_y >= 0 and next_y <= n-1 and borad[next_x][next_y] == 0:
            borad[next_x][next_y] = 1
            move(next_x,next_y,step+1)
            borad[next_x][next_y] = 0 #回退到某个值，其中经过的点赋为0




borad[a][b] = 1#表示马已经走过
move(a,b,1)
print(cnt)