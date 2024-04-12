w = [0,1,2,4,2,5] #重量
v = [0,5,3,5,3,2] #价值

def ks(n,C):
    #基础条件
    if n == 0 or C == 0:
        result = 0
    elif w[n] > C:
        result = ks(n-1,C)
    else:
        tmp1 = ks(n-1,C) #不放这个商品 no
        tmp2 = v[n] + ks(n-1,C-w[n]) #放这个商品的价值
        result = max(tmp1,tmp2)
    return result

n = 5; C = 10
s = ks(5,10)
print(s)

"""
该算法复杂度为O(2**n)

"""