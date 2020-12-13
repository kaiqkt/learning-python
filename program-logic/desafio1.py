for n, n2 in enumerate(range(10, 1, -1)):
    print(n, n2)


#  validar cpf
print(f'\n')

cpf = '168.995.350-09'
cpf_valido = cpf.split('.')
cpf_valido_2 = ''.join((''.join(cpf_valido).split('-')))
print(cpf_valido_2)

b1 = False
b2 = False

n1 = 10
r = 0
for n in cpf_valido_2:
    if n1 < 2:
        break
    else:
        r += int(n) * n1
        print(f'{n} * {n1} = {int(n) * n1}')
        n1 -= 1

r1 = 11 - (r % 11)

if 11 - (r % 11) == 11:
    b1 = True

n1 = 11
r = 0
for n in cpf_valido_2:
    if n1 < 2:
        break
    else:
        r += int(n) * n1
        print(f'{n} * {n1} = {int(n) * n1}')
        n1 -= 1
print(r)
if 11 - (r % 11) == 9:
    b2 = True

cpf_valido = '.'.join(cpf_valido)

if b1 and b2:
    if cpf == cpf_valido:
        print('Cpf Valido')
    else:
        print('Cpf Invalido')