import sqlite3
try:
    conn = sqlite3.connect("database.db")
    cursor=conn.cursor()
    print("Database Connection and creation is successfully created")
    cursor.close()

except sqlite3.Error as error:
    print("Error in creating Database")
finally:
    if(conn):
        conn.close()
        print("Sqlite connection is closed")