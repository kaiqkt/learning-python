from aula14_dados import produtos, pessoas, lista

def aumenta_preco(p):
    p['preco']= round(p['preco'] * 1.20, 2)
    return p


precos = map(aumenta_preco, produtos)

for a in precos:
    print(a)