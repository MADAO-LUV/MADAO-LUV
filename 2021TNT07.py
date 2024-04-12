"""
给定N个数字（包含整数和小数），找到N个数中最大的数字
输入描述：
输入N个数字（N>2），且N个数字之间以英文逗号隔开
输出描述：
输出N个数字中最大的数字
样例输入:
4,8,2
"""
lst = list(map(float,input().split(",")))
res = max(lst)
print(res)