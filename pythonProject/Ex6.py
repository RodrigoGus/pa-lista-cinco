import random


a=[]
p = 0
arr_p = []
m_p = 0
i = 0
arr_i = []
m_i = 0
for r in range(1,11,1):
    # b = float(input(f'insira aqui o {i}° valor:    '))
    b = random.randint(0,9)
    a.append(b)
for n in range(10):
    if a[n] % 2 == 0:
        p += 1
        arr_p.append(a[n])
    else:
        i += 1
        arr_i.append(a[n])
    m_p += a[n]
    m_i += a[n]
m_p / 10
m_i / 10
x = m_p
print(arr_i)
for g in range(10):
    x += arr_i[g]
