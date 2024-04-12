"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。

示例 1：

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15
"""
cost = eval(input()) #用来接收数组
# 将输入每个数以空格键隔开做成数组
N = 1010
memo = [0 for i in range(N)]
def dfs(x):
    if memo[x]:
        return memo[x]
    if x == 0 or x == 1:
        return 0
    else:
        res = min(dfs(x-1)+cost[x-1],dfs(x-2)+cost[x-2])
    memo[x] = res
    return res

print(dfs(len(cost)))