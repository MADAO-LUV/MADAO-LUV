n = eval(input())
maindiag = [0 for x in range(2*n-1)] #主对角线[0,0,0,0,0,0]
subdiag = [0 for x in range(2*n-1)] #负对角线 [0,0,0,0,0,0]
column = [0 for x in range(n)] #列号
rows = [-1 for x in range(n)] #存什么？ [1,3,0,2] 第一行存的入的是第一列，第二行存入的是第三列

def printSolution():
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
def search(row): #0行
    global cnt
    for col in range(n):
        x = row;y = col
        if maindiag[x-y+n-1] == 0 and subdiag[x+y] == 0 and column[y] == 0:
          rows[row] = col #第row行，在第col列放置了一个皇后 范围[0,n-1]
          maindiag[x-y+n-1] = 1 #这个主对角线被占用
          subdiag[x+y] = 1 #副对角线标记被占用
          column[col] = 1 #该列标记被占用了
          if row < n-1:
              search(row+1)
          else: #row == n-1
              cnt += 1
              #printSolution() 可以通过这个来看到方案
        #如果没搜索到什么，便回溯各行各列，以及其主副对角线
          maindiag[x-y+n-1] = 0
          subdiag[x+y] = 0
          column[col] = 0
          rows[row] = -1


search(0)
print(cnt)



