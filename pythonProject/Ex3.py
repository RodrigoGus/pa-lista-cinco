lista = []

for i in range (15):
    valor = float(input(f'insira o {i + 1}° valor:    '))
    lista.append(valor)

y = 1
for valor in lista:
    x = valor % 2
    if x == 0:
        print(f'{y}°: {valor} é par')
    else:
        print(f'{y}°: {valor} é impar')
    y += 1