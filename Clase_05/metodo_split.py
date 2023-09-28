#help(str.split)

cursos = 'Java Javascript Node Python Diseño'
lista_cursos = cursos.split()
print(f'Lista Cursos: {lista_cursos}\ntipo: {type(lista_cursos)}')

cursos_separados_coma = 'java,python,node,javascript,spring'
lista_cursos = cursos_separados_coma.split(sep=',',maxsplit=2)#defaul busca espacios no tiene, pero separa por la ',' solo 2 veces
print(f'Lista Cursos: {lista_cursos}\ntipo: {type(lista_cursos)}')
print(len(lista_cursos))