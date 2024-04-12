"""
输入一个整型数组，数组中的一个或连续多个整数组成
一个子数组，求所有子数组的和的最大值
要求时间复杂度为O(n)

输入:nums = [-2,1,-3,4,-1,2,1,-5,4]
输出:6
解释:连续子数组[4,-1,2,1]的和最大 为6

1.重述问题: 求一个数组中 和最大的子数组
2.找到最后一步: 选择了某个数 作为子数组的最后一个数
3.选择了某个数 作为去了最后一个数的子数组的最后一个数
4.边界:到头的时候 时 return 0
"""
nums = eval(input())
n = len(nums)
ans = -101 #假设数组里面的全是负数时
memo = [0 for i in range(10010)]
#传入的数
def dfs(x):
    res = 0
    if x < 0:
        return 0
    if memo[x]:
        return memo[x]
    res = max(nums[x],dfs(x-1)+nums[x]) #因为是直接取上一个数，就不用枚举了
    memo[x] = res
    return res

for i in range(0,n):
    ans = max(ans,dfs(i))

print(ans)