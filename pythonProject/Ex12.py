import random


a = []
for i in range(1,11,1):
    # b = float(input(f'insira aqui o {i}° valor:    '))
    b = random.randint(0,9)
    a.append(b)
print(a)
print(min(a))