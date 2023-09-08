"""
Combinations, Permutations, Product

Combinações (Combinations) - As ordens não importa
Permutação ( Permutations) - As ordens importa - AMBOS não repetem valores unicos.
Produtos (Product) - As ordens importa e repete valores unicos.
"""
from itertools import combinations, permutations, product

lista = ('Everton', 'Luiz', 'João', 'Anna')
for grupo in combinations(lista, 2):  # Fazendo 1 grupo de "2" pessoas por vez
    print(grupo)
# Como a ordem nao importa, se tiver ('everton', 'luiz'), não terá ('luiz', 'everton'). Os dois são iguais
print()
# Para ter as combinações
for grupo in permutations(lista, 2):
    print(grupo)
# A ordem já importa, terá ('everton', 'luiz') e ('luiz', 'everton')
print()
# Para todas as combinações possiveis, repetindo
for grupo in product(lista, repeat=3):
    print(grupo)
