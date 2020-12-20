from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Kaique', 'nota': 'A'},
    {'nome': 'Luiza', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'F'},
    {'nome': 'Lucio', 'nota': 'D'},
    {'nome': 'Jose', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for a, b in alunos_agrupados:
    va1, va2 = tee(b)

    print(f'Agrupamento: {a}')

    for a in va1:
        print(a)

    qnt = len(list(va2))
    print(f'{qnt} alunos tiraram {a}\n')