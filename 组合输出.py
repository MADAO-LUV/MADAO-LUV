"""
排列与组合是常用的数学方法，其中组合就是从n个元素中抽出了r个元素
(不分顺序且r<=n),我们可以简单地将n个元素理解为自然数1,2,....,n从中任取r个数

现在要求输出所有的组合

顺序：1.依次枚举每个数放哪个位置
2.依次枚举每个位置放哪个数
"""
n,r = map(int,input().split(','))


arr = [0 for i in range(n+1)] #暂时存放结果
cnt = 0
#x 记录当前枚举到哪个位置 start 记录当前位置从几开始枚举
def DFS(x,start):
    # 减枝操作,这里说明它填不满k个数
    # x-1是表达的是已经被选了数 n-start+1得出还有几个数没选
    if (x - 1 + n - start + 1) < r:
        return  # 直接retrun掉

    if x > r:
        for i in range(1,r+1):
            print(arr[i],end = " ")
        print("\n")
        return

#从start开始 ，后面的数肯定没选过
    for i in range(start,n+1):
        arr[x] = i
        DFS(x+1,i+1)
        arr[x] = 0



DFS(1,1)
