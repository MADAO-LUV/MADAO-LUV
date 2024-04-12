lst = input().split()
c = []
for ele in lst:
    a,b = ele.split(',')
    a,b = int(a),int(b)
    c.append((a,b))
    #装入元组中
rows = {} #行字典
cols = {} #列字典
maindiag = {} #主对角线 x + y
subdiag = {} #副对角线 x - y
for item in c:
    x,y = item[0],item[1]
    if x in rows:
        rows[x] += 1 #在该行加1
    else:
        rows[x] = 1 #不在就更新为1
    if y in cols:
        cols[y] += 1
    else:
        cols[y] = 1

    if x+y in maindiag:
        maindiag[x+y] += 1
    else:
        maindiag[x+y] = 1

    if x-y in subdiag:
        subdiag[x-y] += 1
    else:
        subdiag[x-y] = 1

#分别检索出各个字典里面的最大值，然后一起比较
a = max(rows.values())
b = max(cols.values())
c = max(maindiag.values())
d = max(subdiag.values())
print(max(a,b,c,d))
