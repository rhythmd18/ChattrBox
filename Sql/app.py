"""importing the desired libraries"""
import sqlite3

conn = sqlite3.connect("sample.db")

# Create a cursor
c = conn.cursor()

c.execute("SELECT first_name FROM customers WHERE last_name = 'Pal'")
names = c.fetchall()
namesArr = []
for i in range(len(names)):
    if names == []:
        break
    else:
        namesArr.append(names[i][0])

print(names[0][0])
print("Query executed successfully!")
conn.commit()

conn.close()