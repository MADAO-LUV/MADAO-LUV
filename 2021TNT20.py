from itertools import *
n = int(input())
bit = len(str(n))
cnt = 0
for num in permutations("123456789"):
  a,b,c = 0,0,0
  for al in range(bit):  #al是a的位数，肯定是比n短的
    a = int("".join(num[:al+1])) #一个a
    bLast = (n - a) * int(num[-1]) % 10 #c的最后一位数取余后就是b的尾数
    if bLast == 0:
      continue
    bl = num.index(str(bLast)) #根据b的尾数确定b的长度
    if bl <= al or bl >= 8:
      continue
    b = int("".join(num[al+1:bl+1]))
    c = int(" ".join(num[bl+1:]))
    if b % c == 0 and n == a + b // c:
      cnt += 1


print(cnt)