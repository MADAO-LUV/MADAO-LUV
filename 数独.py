"""
数独游戏
递归（暴力搜索）， 回溯
"""
# x为行， y为列 num为要填写的数字
def vaild(x,y,num): #符合条件：true 不符合为：false
    if num in a[x]: #每一行的数字均含1-4（不重复）
        return False
    if num in list(zip(*a))[y]:
        return False #每一列的数字均含有不重复的数

    #检查现在该数字是否在该2*2的数字宫里面
    ax,ay = x//2,y//2 #如果是标准的数独格 需要将函数中所有的2替换为3
    for x in range(2):
        for y in range(2):
            nx,ny = ax*2+x,ay*2+y
            if num == a[nx][ny]:
                return False
    return True

a = [
    list("1234"),
    list("4321"),
    list("0000"),
    list("0000")
]
a = [ [int(x) for x in row] for row in a]
cnt = 0#计算器
def find():
    global cnt
    for i in range(4):
        for j in range(4):
            if a[i][j] == 0:
                for num in (1,2,3,4):
                    if vaild(i,j,num):
                        print(f"{i},{j}--{num} 对")
                        a[i][j] = num #不重复时，就是该数字
                        find()#通过递归调用自己
                        a[i][j]=0 #回溯
                    else:
                        print(f"{i},{j}--{num} 错")
                return
            #在寻找的时候发现1个都不能填入的话，return结束
    print("---found---");cnt+=1#找到了
    for row in a:
        print(row)

find()
print(cnt)
for row in a:
    print(row)


#最终的a还是原来的模样，计算机要测到底，回溯了