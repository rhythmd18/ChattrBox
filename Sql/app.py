"""importing the desired libraries"""
import sqlite3

conn = sqlite3.connect("sample.db")

# Create a cursor
c = conn.cursor()



c.execute("INSERT INTO customers VALUES ('Rhythm', 'Dutta', 'duttarythm@oijo.com')")

print("Query executed successfully!")

conn.close()