t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
u=()
for i in t1:
    if i not in t2:
        u+=(i,)
for i in t2:
    if i not in t1:
        u+=(i,)
print("unique element :",u)