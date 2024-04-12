"""
洛谷 p1443
马的遍历
马走日
"""
def isBule(x):
    if x <= 5:
        return True
    else:
        return False
res = [3,4,4,6,7]
l = -1
r = 5
while (l+1 != r):
    mid = (l + r) // 2
    if isBule(res[mid]):
        l = mid
    else:
        r = mid
print(l)
