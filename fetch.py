import sqlite3

def fetch_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT query
    cursor.execute('SELECT * FROM students')

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    fetch_data()
