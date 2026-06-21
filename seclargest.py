a=(1,8,6,9,5)
b=list(a)
b.sort(reverse=True)
print(b[1])

sl=sorted(set(a))[-2]
print(sl)