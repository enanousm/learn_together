import sqlite3 as sql
url = 'letoapp/database/database.sqlite3'

def buscar_usuario(username):
    instruction = f'''SELECT * FROM letoapp_userdata WHERE username='{username}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data

def organizar_horario(request):
    horarios = ''
    hlu = request.POST.getlist(str('lu'))
    for h in hlu:
        horarios += h
    hma = request.POST.getlist(str('ma'))
    for h in hma:
        horarios += h
    hmi = request.POST.getlist(str('mi'))
    for h in hmi:
        horarios += h
    hju = request.POST.getlist(str('ju'))
    for h in hju:
        horarios += h
    hvi = request.POST.getlist(str('vi'))
    for h in hvi:
        horarios += h
    return horarios

def arreglar_horario(h):
    final = ''
    dia = h[0:2]
    hora = int(h[2])
    if dia == 'lu':
        final += 'Lunes: '
    elif dia == 'ma':
        final += 'Martes: '
    elif dia == 'mi':
        final += 'Miercoles: '
    elif dia == 'ju':
        final += 'Jueves: '
    elif dia == 'vi':
        final += 'Viernes: '
    ##############
    if hora == 1:
        final += '1-2 '
    elif hora == 2:
        final += '3-4 '
    elif hora == 3:
        final += '5-6 '
    elif hora == 4:
        final += '7-8 '
    elif hora == 5:
        final += '9-10 '
    elif hora == 6:
        final += '11-12 '
    elif hora == 7:
        final += '13-14 '
    elif hora == 8:
        final += '15-16 '
    ##############
    return final

def recuperar_horario(horario):
    largo = len(horario)
    lista_horarios = []
    final = ''
    i = 0
    while i < largo:
        dato = horario[i:i+3]
        lista_horarios.append(dato)
        i+=3
    for h in lista_horarios:
        h = arreglar_horario(h)
        final += h
    return final

def separar_horario(horario):
    largo = len(horario)
    lista_horarios = []
    i = 0
    while i < largo:
        dato = horario[i:i+3]
        lista_horarios.append(dato)
        i+=3
    return lista_horarios

def filtrar_ramo(ramo):
    instruction = f'''SELECT * FROM letoapp_userdata WHERE estudiar='{ramo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data

def filtrar_horario(lista_horario,datos):
    final = {}
    for horario in lista_horario:
        for _,first_name,last_name,rol,n_horario,_,email,username in datos:
            if horario in n_horario:
                if username not in final:
                    final[username] = [first_name,last_name,rol,email,'']
                final[username][-1] += horario
    return final

def match(ramo,horario):
    datos = filtrar_ramo(ramo)
    if len(datos) == 0:
        return 0
    n_horario = separar_horario(horario)
    match_final = filtrar_horario(n_horario,datos)
    return (match_final)

print (buscar_usuario('enano_cello'))