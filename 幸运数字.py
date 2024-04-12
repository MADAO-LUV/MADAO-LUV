"""
幸运数，题目：只含有6，8的数才能被称为幸运数
且它们的排列是从小到大进行排列
将6看作0，将8看作1，实质的个数是等比数列
寻找第n个幸运数，并且输出
"""
n = int(input()) #所想要输入的数
s = 0
i = 0
while s<n:
    s = s + 2**(i+1)#计算整个所有的数的数量，第一项是2,等比数列的和
    i += 1
offset = n-(s-2**i)-1
"""
n是我们想要的数的次序，s为整个块的数量（1-i的2的次方之和）
s-2**i (i是最后截止的次方）；n一定包含前2**(i-1)的和 
就是说 s>= n；始终成立，得到n的偏移量之后再减去1，就可以得到n在最后一块的2的i次方中数的次序
因为是从0开始数
"""
#这里要传入我们得到的偏移量
def demail_Num(n):
    fa = ""
    while n:
        res = n%2
        fa = fa + str(res)
        res = res // 2
    return fa
#返回字符串类型

res = demail_Num(offset)#我们还需要为它补上相应的0
res = '0'*(i-len(res)) + res #补零的长度取决于它最终位于哪个2的i次方块中
res = res.replace('0','6').replace('1','8')
print(res)


"""
方案二:
n = eval(input()) #所想要输入的数
s = 0
i = 0
while s<n:
    s = s + 2**(i+1)#计算整个所有的数的数量，第一项是2,等比数列的和
    i += 1
offset = n-(s-2**i)-1
res = bin(offset)[2:] --->bin是自带的函数，作用把十进制转化为二进制，并且开头有--0b ,我们要用[2:]切片
res = '0'*(i-len(res)) + res 补零操作
res = res.replace('0','6').replace('1','8') 替换为幸运数字6，8
print(res)最后输出

"""
