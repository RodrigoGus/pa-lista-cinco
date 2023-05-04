nomes = []

for i in range(10):
    nome = input(f'informe o {i + 1}° nome:    ')
    nomes.append(nome)

i = 1
for nome in nomes:
    print(f'{i}° {nome}')
    i += 1