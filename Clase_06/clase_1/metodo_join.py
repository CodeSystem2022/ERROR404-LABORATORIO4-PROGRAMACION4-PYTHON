#help(str.join) # concatena
tupla_str = ('Hola','Alumnos','Tecnicatura','Universitaria')
mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}')

listas_cursos = ['Java','Python','GO','Angular','Spring']
mensaje =', '.join(listas_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario = {'Nombre':'Brian','Apellido':'Ahumada','Edad': '18'} # join solo funciona con string
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, tipo: {type(llaves)}\n,valores:{valores}, tipo: {type(valores)}')


