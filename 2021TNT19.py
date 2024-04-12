"""




"""
n = int(input())
nums = list(map(int,input().split(',')))
k = int(input())

def heshu(n):
    for x in range(2,n):
        if n%x == 0:
            return True
    return False

res = []
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            res.append(nums[i]+nums[j]+nums[k])
            print(f"{nums[i],nums[j],nums[k]}")

a = set(res) #集合去掉重复的数 list to set
b = 0
for ele in a:
    if heshu(ele):
        b += 1
a = len(a)
print(f"{a},{b}")