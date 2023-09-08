"""
Zip = unindo iteraveis - Uni até a lista menor
zip_longest - Itertools - unir até a maior lista
"""
from itertools import zip_longest, count

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

# Para unir as duas lista, associando Estado com a cidade:
estados_cidades = zip(estados, cidades)
print(next(estados_cidades))
print(list(estados_cidades))
for estad, cidad in estados_cidades:  # Desempacotando
    print(estad, cidad)
print()

# Usando zip_longest - adiciona None aos valores faltando
estados_cidades = zip_longest(estados, cidades, fillvalue='Estado')
for estado, cidades in estados_cidades:
    print(estado, cidades)
print()

indices = count()  # Iterador
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
estados_cidades = zip(indices, estados, cidades)
for index, estado, cidade in estados_cidades:  # Se não tivesse desempacotando, retornava uma tupla!
    print(index, estado, cidade)
    