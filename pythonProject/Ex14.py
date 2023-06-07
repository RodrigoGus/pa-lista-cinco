a = []
b = []

for _ in range(2):
    c = input("digite o nome do aluno: ")
    d = float(input("digite a nota do aluno: "))
    a.append(c)
    b.append(d)
e = input("digite o nome do aluno a pesquisar: ")

if e in a:
    print("aluno encontrado")
    print("nome:", c)
    print("nota:", b)
else:
    print("aluno não cadastrado.")
