"""importing the desired libraries"""
import sqlite3

conn = sqlite3.connect("sample.db")

# Create a cursor
c = conn.cursor()

customers = [
    ("Sagarika", "Pal", "sagarika18jan@adfsdaf"),
    ("Kunal", "Nath", "kunalknath@adfasf"),
    ("Violina", "Bora", "violina@afdasdf")
]


c.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)

print("Query executed successfully!")
conn.commit()

conn.close()