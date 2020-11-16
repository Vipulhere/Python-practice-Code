import sqlite3
conn=sqlite3.connect("database.db")
query="SELECT * FROM STD LIMIT 2;"
try:
    cursor=conn.cursor()
    cursor.execute(query)
    fetch=cursor.fetchall()
    print(fetch,"Record is ")
    conn.commit()
except:
    print("Database Error")
    conn.rollback()
conn.close()