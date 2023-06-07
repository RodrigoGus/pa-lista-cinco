import random

a = []

for i in range(1,11,1):
    # b = float(input(f'insira aqui o {i}° valor:    '))
    b = random.randint(0,9)
    a.append(b)
print(a)
c = int(input('insira um valor a ser procurado na array:    '))

if c in a:
    print(f'o valor {c} está na lista e tem o índice {a.index(c)}')
else:
    print(f'o valor {c} não está na lista :(')