import sqlite3
conn = sqlite3.connect('students.db')

cursor = conn.cursor()

cursor.execute ("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    print(row)

name = "Sauda Haque"
cursor.execute("SELECT * FROM student WHERE name = ?", (name,))
result = cursor.fetchone()

if result == None:
    print("Ingen namn heter så!")
else:
    print(result)

cursor.close()
conn.close()