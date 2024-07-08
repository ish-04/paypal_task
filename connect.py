import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    mark1 real,
    mark2 real,
    mark3 real
)
''')

# Insert data into the table
students = [
    (1, 'Anita', 21, 67.5, 70, 88.5),
    (2, 'Anjali', 20, 97.5, 80, 70),
    (3, 'Bhabhati', 21, 90, 98.5, 96),
    (4, 'Swetha', 19, 45, 46, 63.5),
    (5, 'Tarun', 22, 45, 48, 90)
]

cursor.executemany('''
INSERT INTO students (id, name, age, mark1, mark2, mark3)
VALUES (?, ?, ?, ?, ?, ?)
''', students)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

