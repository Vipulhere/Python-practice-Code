import sqlite3
conn=sqlite3.connect("database.db")
query="UPDATE STD SET age=25 WHERE name='bob';"
try:
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("record is updated ")
except:
    print("Error in updating record")
    conn.rollback()
conn.close()