"""
Funcoes (def) em Python - *args **kwargs
* serve para desempacotar
"""


def func(*args, a2=None):
    # args = list(args)
    print(args)


def func_1(**kwargs):
    # args = list(args)
    print(kwargs)

    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


func(1, 2, 3, 4, 5, a2='Kaique')

lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista

func_1(nome='Kaique', idade=18)

