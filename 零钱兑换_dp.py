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
4.不选硬币 下标为0的时候

原问题答案 = 用最少的硬币数 凑出 amount-5 一直进行划分
"""
coins = eval(input())
amount = int(input())
n = len(coins)
f = [int(1e9) for i in range(10010)] #取一个很大的值，让amoumt里面的数，永远取不到
f[0] = 0 #因为是逆推 所以第0个要初始化为0

for i in range(1,amount+1):
    for j in range(0,n):
        if i >= coins[j]:
            f[i] = min(f[i],f[i-coins[j]]+1)

print(-1 if f[amount] == int(1e9) else f[amount])
