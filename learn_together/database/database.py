import sqlite3

connection = sqlite3.connect('learn_together/database/lt_bd.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS userdata(
               nombre text,
               apellidop text,
               sexo text,
               correo text,
               contraseña text,
               rol text,
               horarios text
    )
''')

instruction = 'INSERT INTO userdata VALUES({},{},{},{},{},{},{})'.format('Juan','Perez','Hombre','jperez','hola1234','123456789-0','lu7,ma8,vi3')
cursor.execute(instruction)


connection.commit()
connection.close()

