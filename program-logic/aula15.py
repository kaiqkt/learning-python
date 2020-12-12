"""
For in em Python
Iterando strings com for
Funcao range(start=0, stop, step=1)
continue - pula para o proximo laco
break - termina o laco
"""
texto = 'Python'

x = 0

for letra in texto:
    print(letra)

for i, n in enumerate(texto):
    print(i, n)

for n in range(0, 12, 2):
    print(n)

#  divisivel por 20
for n in range(100):
    if n % 20 == 0:
        print(n)

nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
    print(nova_string)