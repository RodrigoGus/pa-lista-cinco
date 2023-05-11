import random
a = []
for r in range(10):
    x = (random.randint(0,100))
    a.append(x)
print(a)
for n in range(0, 10, 2):
    y = a[n]
    y *= 3
    a.pop(n)
    a.insert(n, y)
    n += 2
for g in range(1, 10, 2):
    y = a[g]
    y /= 2
    a.pop(g)
    a.insert(g, y)
    g += 2
print(a)