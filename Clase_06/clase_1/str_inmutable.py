help(str.capitalize)# el primer caracter lo convierte en mayuscula el resto en minuscula
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id:{id(mensaje1)}\nmensaje2: {mensaje2}, id:{id(mensaje2)}') 

mensaje1 += 'Adios'
print(f'mensaje1: {mensaje1}, id:{id(mensaje1)}')
