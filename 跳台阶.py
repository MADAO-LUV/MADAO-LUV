"""
一个楼梯共有n级台阶,每次可以走一级或者两级，问从第0级台阶走到第n级台阶一共有多少种方案
"""


n = eval(input())
N = 1e6
m = [0 for i in range(int(N))]
def fibonaci(x):
    if x == 1 or x == 2:
        return 1
    if m[x] != 0:
        return m[x]
    else:
        m[x] = fibonaci(x-1) + fibonaci(x-2)
        return m[x]

s = fibonaci(n)
print(s)

"""
递推形式
n = eval(input())
newf,tmp1,tmp2 = 0,1,2
for i in range(n-2):
  newf = tmp1 + tmp2
  tmp1 = tmp2
  tmp2 = newf
print(newf)
"""