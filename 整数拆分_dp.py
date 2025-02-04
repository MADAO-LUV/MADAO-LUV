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
n = eval(input())
f = [0 for i in range(110)]
f[0] = 1
for i in range(1,n+1):
    for j in range(1,i):
        #保留原数 比较两者之间的大小
        f[i] = max(f[i],max(j*(i-j),f[i-j]*j))
print(f[n])