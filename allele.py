t = (1, 2, 3, 4, 5)

all_int = True

for i in t:
    if not isinstance(i, int):
        all_int = False
        break

print(all_int)

t = (1, 2, 3, 4, 5)

print(all(isinstance(i, int) for i in t))
