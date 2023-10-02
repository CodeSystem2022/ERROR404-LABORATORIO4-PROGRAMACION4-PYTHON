# dar formato a un string 
nombre = 'Brian'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d' %(nombre, edad) # %s = String %d = Foat double 
#print(mensaje_con_formato)
persona = ('carla','gomez', 5000.0000)
mensaje_con_formato = 'hola %s %s . Tu sueldo es %.2f ' #%persona # pasamos el objeto 

#print(mensaje_con_formato % persona) # se lo pasamos directamente despues de la cadena

nombre = 'Juan'
edad = 19
sueldo = 3000
mensaje_con_formato  = 'Nombre {} Edad {} sueldo {:.2f}'.format(nombre,edad,sueldo)
#print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} sueldo {2:.2f}'.format(nombre,edad,sueldo)
#print(mensaje)

mensaje = 'nombre {n} edad {e} sueldo {s}'.format(n=nombre,e=edad,s=sueldo)
#print(mensaje)

diccionario = {'nombre':'Ivan','Edad':35,'sueldo':8000.000}
mensaje = 'Nombre {dic[nombre]} Edad {dic[Edad]} Sueldo {dic[sueldo]:2f}'.format(dic=diccionario)
print(mensaje)

