import math
from decimal import Decimal
# manejo de valores infinitos
infinito_positivo = float('inf') # inf es el valor infinito en python
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf') #-inf es el valor infinito en python
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

# modulo math
print("--------------Modulo math--------------")

infinito_positivo = math.inf # valor infinito en math en python
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')

#Modulo decimal
print("--------------Modulo decimal--------------")
infinito_positivo = Decimal('Infinity') # valor infinito en decimal en python
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('-Infinity')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')


