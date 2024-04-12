"""
给定一个正整数n，将其拆分为k个正整数的和(k>=2)
并使这些整数的乘积最大化
返回你可以获得的最大乘积

示例1:
输入:n=2
输出:1
解释:2 = 1 + 1, 1 * 1 = 1

1.重述问题：将一个正整数n，才分为k个正整数达到和
2.最后一步:拆除第k个数
3.去掉最后一步:拆除第k-1个数
4边界就是 k<2
"""
n = int(input())
memo = [0 for i in range(110)]
def dfs(x):
    if memo[x]:
        return memo[x]
    if x < 0:
        return 1
    res = 0
    #不能拆除个0 因为i为0的时候 会一直往下递归
    for i in range(1,x):
        res = max(res,max(i*(x-i),dfs(x-i)*i))#选的那个数
    memo[x] = res
    return res
print(dfs(n))
"""
对于(x-i)*i的解释:
并不是确保分成了两份，因为x大于i，所有x永远不会为0，
也就保证了一定分成了大于两份
"""