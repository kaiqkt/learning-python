"""
Lambda
"""


def funcao(arg, arg_2):
    return arg * arg_2


var = funcao(2, 2)

print(var)

# a = lambda x, y: x * y

# print(a)

lista = [
    ['P0', 15],
    ['P2', 18],
    ['P55', 17],
    ['P4', 16]
]


def func(item):
    return item[0]


lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
print(sorted(lista, key=lambda i: i[1]))
