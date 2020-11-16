import sqlite3
conn=sqlite3.connect("database.db")
query="DELETE FROM STD WHERE name='BOB';"
try:
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Record is successfully deleted")
except:
    print("error into deletion of record")
    conn.rollback()
conn.close()
