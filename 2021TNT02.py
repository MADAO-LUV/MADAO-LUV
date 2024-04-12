"""
给定一个正整数N，计算出1到N之间所有奇数的和
输入一个正整数N
输出1到N之间（包含1和N）所有奇数的和

"""

n = int(input())
res = 0 #累加器
for i in range(1,n+1):
    if i % 2 == 1:
        res = res + i
print(res)

"""
方法二: 因为1是为奇数，那么我们将step（步长设为2）则每次遍历的数都为奇数
再累加到一起即可
n = eval(input())
res = 0
for i in range(1,n+1,2):
    res = res + i
print(res)


"""