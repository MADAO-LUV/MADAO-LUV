"""
输入多个英文单词(单词都为小写字母）,然后按字典顺序排序输出
注:单词首字母相同时就比较第二个字母，以此类推
输入描述:
输入多个由小写字母组成的英文单词，单词之间以一个英文逗号隔开
输出描述:
按字典顺序排序输出，且单词之间以一个英文逗号隔开

"""
lst = input().split(',')
lst.sort()
res = ",".join(lst)
print(lst)