# Find the second smallest element in a tuple.
t = (5, 8, 2, 8, 10, 10, 7)
a=set(t)
t=sorted(set(a))
print(t[-2])