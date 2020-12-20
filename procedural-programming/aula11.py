"""
Geradores, iteradores e iteraveis em python
"""

import sys

lista = (x for x in range(1000000))


print(sys.getsizeof(lista))