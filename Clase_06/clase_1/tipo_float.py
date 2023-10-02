# Profundizando en el tipo float
a = 3.0
print(f'Tipo float: {a:.2f}')

# Constructor de tipo float -> puede recibir int str
a = float(10) # le pasamos un tipo entero (int)
print(f'Tipo float: {a:.2f}')

a = float('10') # le pasamos un tipo String
print(f'Tipo float: {a:.2f}')

# Notación exponencial (valores positivos o negativos)
a = 3e5 # valor agregamos 5 ceros despes del 3
print(f'exponencial: {a:.2f}')

a = 3e-5
print(f'exponencial: {a:.5f}') # :.5f mostramos los 5 ceros de la variable a

# Cualquier calculo que incluya un float, todo cambia a float
a = 4.0 + 5
print(f"En la suma de un entero y un decimal cambia a float: {a}, estipo {type(a)}" )

