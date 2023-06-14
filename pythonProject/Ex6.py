import random


a = []  # lista de todos os números
q_p = 0  # quantidade de números pares
arr_p = [] # lista dos números pares
m_p = 0 # media da soma dos pares
q_i = 0 # quantidade de números impares
arr_i = [] # lista dos números impares
m_i = 0 # media da soma dos pares
sm_t = 0
for r in range(1, 11, 1):
    # b = float(input(f'insira aqui o {i}° valor:    '))
    b = random.randint(0, 9)
    a.append(b)
for n in range(10):
    if a[n] % 2 == 0:
        q_p += 1
        arr_p.append(a[n])
        m_p += a[n]
        sm_t += a[n]
    else:
        q_i += 1
        arr_i.append(a[n])
        m_i += a[n]
        sm_t += a[n]
m_p /= 10
m_i /= 10
sm_t /= 10
print(f''' {a}
a) - A quantidade de números pares. {q_p}
b) - Os números pares. {arr_p}
c) - A quantidade de números ímpares. {q_i}
d) - Os valores ímpares. {arr_i}
e) - A média dos valores pares. {m_p}
f) - A média dos valores ímpares. {m_i}
g) - A média da soma dos valores pares mais os valores ímpares. {sm_t}
''')
