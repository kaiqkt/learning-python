"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f = Quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Es
"""

num_1 = 10
num_2 = 2
divisao = 1 / 2
print('{:.2f}'.format(divisao))

nome = 'Luiz Otavio'
print('{:.2s}'.format(nome))

print(f'{num_1:0^10}')
print(f'{num_1:0>10}')
print(f'{num_1:0<10}')

print(f'{num_1:0<10.2f}')

print(f'{nome:#^36.14s}')

print('{n:#^36.14s}'.format(n=nome))

nome = nome.center(20, '#')
nome = nome.ljust(20, '#')
nome = nome.rjust(20, '#')
print(nome.upper())
print(nome.lower())
print(nome.title())
