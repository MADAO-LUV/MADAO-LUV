# // 整除 % 求余
a = [
    [1,2,3,55],
    [4,5,6,66],
    [7,8,9,77],
    [10,11,12,88]
]
#定义了一个二维数组，输出第8个数
n = 7 #索引号为7
x = n // 4
y = n % 4 #实际的长度为4 但是索引是从0-n-1
print(a[x][y])