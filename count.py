"""
Count - itertools
Função count -  retorna um iterador, fornece um contador, pode-se usar NEXT; Diferente do range, pois,
é um iteravel!
Count é importante, pois, não preciso fazer o famoso "contador"
"""
# obs: Aula passada sobre zip
import itertools
from types import GeneratorType


var = zip('Alo', 'Alo')  # iterage sobre str, fazendo um iterador
print(next(var))
print(isinstance(var, GeneratorType))  # Verificando se é um gerador!

# Para transforma em um gerador:
var = ((x, y) for x, y in zip('Alo', 'Alo'))
print(isinstance(var, GeneratorType))  # gerador
print()

contador = itertools.count(start=5, step=0.05)  # Posso indicar de onde começa, e de quantos em quantos.
for valor in contador:
    print(round(valor, 2))  # função round - arrendonda "2" casas decimais
    if valor >= 15:
        break
