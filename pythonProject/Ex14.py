a = []
b = []
for r in range(5):
    c = input("digite o nome do aluno para adicionar: ")
    d = float(input("digite a nota do aluno adicionado: "))
    a.append(c)
    b.append(d)
e = input("digite o nome do aluno para pesquisar: ")
if e in a:
    indice = a.index(e)
    d = b[indice]
    print("aluno:", e)
    print("nota:", d)
else:
    print("aluno não cadastrado.")