import random

a = []
b = []
a2 = []
b2 = []

for i in range(0, 10, 2):
#    x = int(input(f'insira o {i + 1}° valor:    '))
    x = int(random.randint(100))
    a.append(x)
    for i2 in range(1, 10, 2):
#        x = int(input(f'insira o {i + 1}° valor:    '))
        x = int(random.randint(100))
        a.append(x)

y = 1
a2.copy(a)
b2.copy(b)