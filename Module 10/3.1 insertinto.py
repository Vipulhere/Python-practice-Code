import sqlite3
conn=sqlite3.connect("database.db")
query="INSERT into STD(name,age,dept)values ('bob',20,'CS');"
try:
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Our record is inserted into database")
except:
    print("Error in database insert record")
    conn.rollback()
conn.close()