import math
from decimal import Decimal
# Tipo NaN
# puede ser resultado de una exprecion matematica

#NaN (not number)
a = float('nan')

print(f'resultado: {a}')
print(f'Es de tipo NaN(not a number)?: {math.isnan(a)}')
# módulo math
a = Decimal('NaN')
print(f'Es de tipo NaN(not a number)?: {math.isnan(a)}')