"""
For/ Else em Python
"""

lista = ['A', 'B', 'C']

for x in lista:
    if x.lower().startswith('a'):
        print('ok', x)
        break
else:
    print('not ok')