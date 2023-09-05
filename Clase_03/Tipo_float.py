#Profundizando en tipo float

a =3.0
print(f'a: {a:.2f}')

#Constructor de tipo float -> puede recibir int y str
a =float(10) # le pasamos un tipo entero
a=float('12') #le pasamos un string
print(f'a: {a:.2f}')

#Notacion exponencial > valores positivos o negativos
a = 3e5
print(f'a: {a}')

a = 3e-5
print(f'a: {a:.5f}')

#Cualquier calculo que incluya un float, todo cambia a Float
a= 4.0 + 5
print(a)
print(type(a))