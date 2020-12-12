"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +, min, max
range
"""
a = ['A', 'B', 'C']

print(a[:len(a)])

l1 = [1, 2, 3]
l2 = [4, -55, 5, 6]
l3 = l1 + l2
#
# l2.append('b')  # insere no final da lista
print(l2)
# l2.insert(0, 'ba')  # insere no indice escolhido
l2.pop()  # deleta do final da lista
print(l2)

del(l3[3:5])
print(l3)

print(max(l2))  # o maior numero na list
print(min(l2))  # o menor numero na list

l4 = list(range(1, 10))
print(l4)
for valor in l4:
    print(valor)

