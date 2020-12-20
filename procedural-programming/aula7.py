"""
Dicionario em python
lista que possui chave valor
"""

# d1 = {'chave1':'valor da chave'}
# d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
# d1['nova_chave'] = 'valor da chave'
# d1 = {
#     'str': 'valor',
#     "123": 'Outro valor',
#     "chave3": 'Tupla'
# }

# d1.update({'str': 'nova_valor'})
# d1.pop('chave3')
# del d1['str']
#
# print(123 in d1.keys())
# print('Tupla' in d1.values())
#
# print(len(d1))

# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))

cliente = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otavio'
    },
    'cliente2': {
        'nome': 'Kaique',
        'sobrenome': 'Gomes'
    }
}

for clientes_k, clientes_v in cliente.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

import copy

c = copy.deepcopy(cliente)
