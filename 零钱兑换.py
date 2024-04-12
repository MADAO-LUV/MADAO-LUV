"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

1.用最少的硬币数凑出amount
2.选择某一个硬币，使得金额筹到了amount
3.去掉最后一步，问题变成了用最少的硬币数，凑出amount-最后一个硬币
4.当amount < 0 时有返回无限值 可以选一个较大的数来当作无限值
当amount == 0 的时候返回0 因为已经到底部了 完成既定的目标了

原问题答案 = 用最少的硬币数 凑出 amount-5 一直进行划分
"""
coins = eval(input()) #这个是硬币列表
amount = int(input()) #这个是数额列表
memo = [0 for i in range(10010)]
def dfs(amount):
    n = len(coins)
    if memo[amount]:
        return memo[amount] #这个是已经计算过后的数了
    if amount == 0: #当amount数额被满足后
        return 0
    if amount < 0:
        return int(1e9)
    res = int(1e9)
    for i in range(0,n):
        if amount >= coins[i]:
            res = min(res,dfs(amount-coins[i])+1)
    memo[amount] = res
    return res

ans = dfs(amount)
print(-1 if ans == int(1e9) else ans)
