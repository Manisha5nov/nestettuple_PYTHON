a=(1,2,3,4,5)
n=2
n=n%len(a)
r=a[n:] + a[:n]
ro=a[-n:] + a[:-n]
print(r)
print(ro)