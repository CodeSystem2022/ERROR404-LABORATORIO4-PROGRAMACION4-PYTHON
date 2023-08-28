from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion !=5:
    try:
        print('Opciones: ')
        print('1. Listar usuarios')
        print('2. Agregar usuario')
        print('3. Modificar usuario')
        print('4. Eliminar usuario')
        print('5. Salir')
        opcion = int(input('DIgite la opción (1-5): '))

        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        elif  opcion ==2:
            username_var = input('Digite el nombre de usuario: ')
            password_var = input('Digite su contraseña: ')
            usuario = Usuario(username=username_var, password=password_var)
            usuario_insertado = UsuarioDAO.insertar(usuario)
            log.info(f'Usuario insertado: {usuario_insertado}\n')
        elif opcion ==3:
            try:
                id_usuario_var = int(input(f'Digite el id del usuario a modificar: '))
                username_var = input('Digite el nombre del usuario a modificar: ')
                password_var = input('Digite la contraseña del usuario a modificar: ')
                usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
                usuario_actualizado = UsuarioDAO.actualizar(usuario)
                log.info(f'Usuario actualizado: {usuario_actualizado}\n')
            except ValueError as e:
                print("El id del usuario debe ser un valor numérico\n")
        elif opcion ==4:
            try:
                id_usuario_var = int(input(f'Digite el id del usuario a eliminar: '))
                usuario = Usuario(id_usuario=id_usuario_var)
                usuario_eliminado = UsuarioDAO.eliminar(usuario)
                log.info(f'Usuario eliminado: {usuario_eliminado}\n')
            except ValueError as e:
                print("El id del usuario debe ser un valor numérico\n")
    except ValueError as e:
        print("La opción seleccionada debe ser un valor numérico\n")
else:
    log.info('Salimos de la aplicación. Hasta pronto!!')