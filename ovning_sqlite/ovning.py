import sqlite3
conn = sqlite3.connect('students.db')

 
#användas för att köra SQL-kommandon
cursor = conn.cursor()
 
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                age INTEGER,
                grade TEXT NOT NULL
                )
               
''')
cursor.execute ("SELECT * FROM student")
rows = cursor.fetchall()
for row in rows:
    print (row)
   
conn.commit () # sparar ändringar
cursor.close ()
conn.close()