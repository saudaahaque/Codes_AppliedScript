
import sqlite3
conn = sqlite3.connect('sauda_databas2.db')

cursor = conn.cursor()

cursor.execute
('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    age (INTEGER),
    grade (TEXT)           
)              
''')
conn.commit()
cursor.close()
conn.close()


#  TEXT NOT NULL UNIQUE = obligatorisk och unikt värde, får ej förekomma två gånger
#  TEXT NOT NULL = obligatorisk värde


