"""
Split, Join, Enumerate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
"""

string = 'A lamina que nao se ve é a mais mortifera, Zed'
lista = string.split(',')
lista_2 = string.lower().split(' ')
string_2 = ','.join(lista_2)
print(string_2)
print(lista_2)
c = 0
for valor in lista_2:
    if valor.endswith(','):
        x = valor[0:len(valor) - 1]
        del(lista_2[c])
        lista_2.insert(c, x)
        print(valor[0:len(valor) - 1])
    print(lista_2.count(valor))
    c += 1
print(lista_2)

for valor in lista:
    print(valor.strip())

for v1, v2 in enumerate(lista_2):
    print(v1, v2, lista_2[v1])
