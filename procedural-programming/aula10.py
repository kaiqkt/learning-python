"""
Dictionary comprehensions
"""

lista = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

# d1 = {x.upper(): y*2 for x, y in lista}
d1 = {f'key_{x}': x**2 for x in range(5)}

print(d1)