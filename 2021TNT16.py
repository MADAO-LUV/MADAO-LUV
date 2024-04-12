"""

小朋友是围成一圈的,n个次报数为一个周期，且只有一个小朋友报错
0的时候是过的意思,到n的时候就为过
"""

n = eval(input())#小周期
a = list(eval(input()))
c = 0
val = 0
for v in a:
    c += 1
    val += 1
    if c>n:
        c = 1
    if (val%3==0 or '3' in str(val)) and v != 0:
        print(c) #小朋友的编号 过的时候报错了
        break
    if v != val:
        print(c) #正常的时候报错了
        break