"""
Groupby - agrupamento de valores
tee - faz duas copias
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Everton', 'nota': 'A'},
    {'nome': 'Anna', 'nota': 'A'},
    {'nome': 'Paulo', 'nota': 'B'},
    {'nome': 'Fernanda', 'nota': 'C'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'José', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'Mario', 'nota': 'D'},
    {'nome': 'Roberta', 'nota': 'E'},
    {'nome': 'Rafael', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Gabriel', 'nota': 'C'},
    {'nome': 'Julia', 'nota': 'C'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
    {'nome': 'Rodolfo', 'nota': 'D'},
]

ordernar = lambda item: item['nota']
alunos.sort(key=ordernar) # Ordenando por nota
alunos_agrupados = groupby(alunos, ordernar) # agrupando cada aluno por nota

for nota, agrupamento_alunos in alunos_agrupados:
    copia1, copia2 = tee(agrupamento_alunos)

    print(f'Nota: {nota}')

    for alunos in copia1:
        print(f'\t {alunos}')
    quantidade = len(list(copia2))
    print(f'Quantidade de alunos com {nota}: {quantidade}')
    print()