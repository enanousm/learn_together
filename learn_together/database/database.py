import sqlite3

conexion = sqlite3.connect('learn_together_bd')
cursor_bd = conexion.cursor()

def tabla_existe(nombre_tabla):
    cursor_bd.execute('''SELECT COUNT(name) FROM  SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombre_tabla))
    if cursor_bd.fetchone()[0] == 1:
        return True
    else:
        
        return 0