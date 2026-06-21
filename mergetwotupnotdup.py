# Merge two tuples without duplicates.
a=(1,5,6,8)
b=(1,7,3,2)
tup=tuple(set(a+b))
print(tup)

tup1=()
for i in a+b:
    if i not in tup1:
        tup1+=(i,)
print(tup1)