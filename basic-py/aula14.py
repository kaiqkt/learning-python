"""
iterando string com while
"""

frase = 'o rato roeu a roupa do rei de roma'
frase_len = len(frase)
print(frase_len)
x = 0
nova_string = ''

input_user = input("Qual?: ")

while x < frase_len:
    # print(frase[x], x)
    letra = frase[x]
    if letra.__eq__(input_user):
        nova_string += letra.upper()
    else:
        nova_string += frase[x]
    print(nova_string)
    x += 1
print(nova_string)
