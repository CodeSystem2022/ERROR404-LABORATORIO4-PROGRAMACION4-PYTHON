# Bool contiene los valores de True y False
# Los tipos numericos, es false para el 0, true para los demas valores
valor = 0
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')
#cualquier numero fuera del cero es verdadero
valor = -1
resultado = bool(valor)
print(f'valor: {valor}, resultado : {resultado}')

print("---------------String--------------")
#tipo string -> False "", tue demas valores
valor = ""
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')
print("-----------palabra----------------")
valor = "hola"
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')

#Tip Colecciones -> false para las colecciones vacias, tru para todas las demas
#lista
valor = [2,3,4]
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')
print("----------sin nada----------")
valor = []
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')

print("------------Tupla--------------")
#tupla
valor = (1,2,3)
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')

print("-----------sin nada--------------")
valor = ()
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')

#Diccionario
print("----------------diccionario-------------")
valor = {1:"hola",2:"gym",3:"comida"}
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')

print("---------sin nada----------------")
valor = {}
resultado = bool(valor)
print(f'valor :{valor}, resultado :{resultado}')

# Sentencia de control con bool
if '':#Tipo String represantra false, verdadero cuando contiene valor
    print('Regresa verdadero')
else:
    print('Regresa falso')

# cilos
print("----------------cilos-------------")
variable = 9
while variable:
    print("regresa verdadero")
    break
else: 
    print("Regresa falso")

