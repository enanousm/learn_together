import sqlite3 as sql
url = 'letoapp/database/database.sqlite3'

def search_user(username):
    instruction = f'''SELECT * FROM letoapp_horario WHERE username='{username}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data

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