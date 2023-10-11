import sqlite3 as sql
url = 'learn_together/database/database.db'

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

def insert_row(nombre, apellido, sexo, correo, contraseña, rol, horario):
    instruction = f'''INSERT INTO userdata VALUES('{nombre}','{apellido}','{sexo}','{correo}','{contraseña}','{rol}','{horario}')'''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    c.commit()
    c.close()

def update_horario(correo,nuevo_horario):
    instruction = f'''UPDATE userdata SET horarios='{nuevo_horario}' WHERE correo IS '{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    c.commit()
    c.close()

def delete_user(correo):
    instruction = f'''DELETE FROM userdata WHERE correo IS '{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    c.commit()
    c.close()

def search_user(correo):
    instruction = f'''SELECT * FROM userdata WHERE correo IS '{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data[0]

def search_horario(correo):
    instruction = f'''SELECT horarios FROM userdata WHERE correo IS '{correo}' '''
    c = sql.connect(url)    
    cursor = c.cursor()
    cursor.execute(instruction)
    data = cursor.fetchall()
    c.commit()
    c.close()
    return data[0][0]

print(search_user('jureta'))
print(search_horario('jureta'))