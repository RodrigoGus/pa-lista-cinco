import random


a = []
for i in range(1,31,1):
    # b = float(input(f'insira aqui o {i}° valor:    '))
    b = random.randint(0,9)
    a.append(b)
print(a)
a.reverse()
print(a)