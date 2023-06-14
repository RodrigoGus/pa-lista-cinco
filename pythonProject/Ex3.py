a = []
for i in range (15):
    b = float(input(f'insira o {i + 1}° valor:    '))
    a.append(b)
y = 1
for b in a:
    x = b % 2
    if x == 0:
        print(f'{y}°: {b} é par')
    else:
        print(f'{y}°: {b} é impar')
    y += 1