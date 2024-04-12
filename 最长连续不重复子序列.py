nums = eval(input())
N = 3010
n = len(nums)
f = [0 for i in range(N)]


for i in range(0,n):
    f[i] = 1
    for j in range(0,i):
        if nums[j] < nums[i]:
            f[i] = max(f[i],f[j]+1)

res = 0
for k in range(0,n):
    res = max(res,f[k])
print(res)