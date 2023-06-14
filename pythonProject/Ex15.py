import random


a = []
for r in range(20):
    b = random.randint(0,9)
    # b = int(input("digite um valor inteiro: "))
    a.append(b)
print(a)
c = len(a)
for r in range(c // 2):
    a[r], a[c - 1 - r] = a[c - 1 - r], a[r]
print(a)
