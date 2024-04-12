"""
编程实现：有一个N*N的矩阵方格和N个棋子，现在需要将N个棋子按需求
放置到矩阵方格中。要求如下：
1.任意两个棋子不能在同一行
2.任意两个棋子不能在同一列
3.任意两个棋子不能在同一对角线上（下图红色线段都为对角线）
根据以上要求，问N个棋子放置到N*N矩阵方格中有多少种放置方案
例如：4*4的矩阵方格，4个棋子，有2种放置方案

N皇后问题
"""
n = eval(input())
maindiag = [0 for x in range(2*n-1)] #主对角线
subdiag = [0 for j in range(2*n-1)] #副对角线
column = [0 for x in range(n)] #列号
rows = [-1 for x in range(n)] #存什么? 第一行存入的是第一列 第二列存入的是第二列

def printSolution():
    #遍历所有的点
    for i in range(n):
        for j in range(n):
            if rows[i] == j:
                print('Q',end=" ")
            else:
                print('0',end=" ")
        print()
    print()

#递归，数组，循环
cnt = 0
def search(row):
    global cnt
    for col in range(n):
        x = row#行
        y = col#列
        if maindiag[x-y+n-1] == 0 and subdiag[x+y] == 0 and column[y] == 0:
            rows[row] = col #第row行，在第col列放置一个皇后，范围[0,n-1
            maindiag[x-y+n-1] = 1 #这个主对角线被占用
            subdiag[x+y] = 1 #副角线被占用了
            column[col] = 1 #该列标记被占用
            if row < n-1:
                search(row+1)
            else:
                cnt += 1
                printSolution()
            maindiag[x-y+n-1] = 0
            subdiag[x+y] = 0
            column[col] = 0
            rows[row] = -1

search(0)
print(cnt)