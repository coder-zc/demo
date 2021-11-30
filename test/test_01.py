vote=["鲁智深","柴进","宋江","吴用","林冲","卢俊义","柴进","柴进","孙二娘","史进","吴用","卢俊义","柴进","林冲","宋江","宋江","卢俊义","吴用","吴用"]
d={}
for i in vote:
    d[i]=vote.count(i)
l=list(d.items())
l.sort(key=lambda x:x[1],reverse=True)
for i in range(len(l)):
    print(l[i][0],end="\t")
    print(l[i][1],end="\n")