import sqlite3 as sql
url = 'learn_together/database/database.db'

#crear la tabla si esta no existe#
c = sql.connect(url)
cursor = c.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS userdata(
               nombre text,
               apellido text,
               sexo text,
               correo text,
               contraseña text,
               rol text,
               horarios text
    )
''')
c.commit()
c.close()

#insertar nuevo usuario en la base de datos#
def insert_row(nombre, apellido, sexo, correo, contraseña, rol, horario):
    instruction = f'''INSERT INTO userdata VALUES('{nombre}','{apellido}','{sexo}','{correo}','{contraseña}','{rol}','{horario}')'''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    c.commit()
    c.close()

#actualizar horario del usuario#
def update_horario(correo,nuevo_horario):
    instruction = f'''UPDATE userdata SET horarios='{nuevo_horario}' WHERE correo='{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    c.commit()
    c.close()

#borrar usuario de la base de datos#
def delete_user(correo):
    instruction = f'''DELETE FROM userdata WHERE correo='{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    c.commit()
    c.close()

#buscar y retornar todos los campos del usuario#
def search_user(correo):
    instruction = f'''SELECT * FROM userdata WHERE correo='{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data[0]
    #retorna una tupla

#buscar y retornar SOLO EL HORARIO del usuario#
def search_horario(correo):
    instruction = f'''SELECT horarios FROM userdata WHERE correo='{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data[0][0]
    #retorna un string

print(search_user('jureta'))
print(search_horario('jureta'))