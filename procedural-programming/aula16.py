
from functools import reduce

from aula14_dados import lista, produtos

soma_lista = reduce(lambda ac, p: round(p['preco'] + ac, 2), produtos, 0)
print(round(soma_lista/ len(produtos), 2))