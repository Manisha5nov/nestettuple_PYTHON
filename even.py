# Find all even numbers in a tuple.
t = (5, 8, 2, 8, 10, 10, 7)
even=[]
for i in t:
    if i%2==0:
        even.append(i)
        
print(even)

