# profundizando en los sistemas de numeracion

#Sistema decimal
decimal = 73
print(f'decimal = {decimal}')

#Sistema binario
binario = 0b1010 # valor 10
print(f'Binario = {binario}')

# Sistema octal
octal = 0o12 # valor 10
print(f'Octal = {octal}')

#Sistema hexadecimal
hezadecimal = 0xA # valor 10
print(f'hezadecimal = {hezadecimal}')

#Cambiando String a decimal
a = int('23',10) # 10 es la base dice que estamos manejando numero decimales
print(f'de String a decimal = {a}')

# base binario de string a binario
a = int('10111',2) #base para vinario es 2
print(f'String a binario: {a}') 

#base octal de string a octal 
a = int('27', 8) # base 8 para octal
print(f'String a octal: {a}')

#base de hezadecimal de string a hezadecimal
a = int('17', 16) #base de 18 para hezadecimal
print(f'String a hezadecimal: {a}')

# base 5 sus valores son de 0 a 4
a = int('34', 5) # base 5  
print(f'Base 5 sale error si se pasa de la base: {a}')

