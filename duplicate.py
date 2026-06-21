# Find duplicate elements in a tuple.
n=(8,5,5,6,8,9)
dup=[]
for i in n:
    if n.count(i)>1 and i not in dup:
        dup.append(i)
print("duplicate elements :",tuple(dup))
