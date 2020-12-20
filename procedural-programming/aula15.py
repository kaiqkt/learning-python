from aula14_dados import produtos, pessoas, lista

def filtra(p):
    if p['idade'] < 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)