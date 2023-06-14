a = []
for i in range(10):
    b = input(f'informe o {i + 1}° nome:    ')
    a.append(b)
i = 1
for b in a:
    print(f'{i}° {b}')
    i += 1