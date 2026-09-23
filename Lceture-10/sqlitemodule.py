import sqlite3 

conn = sqlite3.connect('mydatabas.db') 
cur = conn.cursor 

cur.execute() 


cur.execute()
cur.execute() 
cur.execute() 

conn.commit() 

cur.execute() 
rows = cur.fetchall()  

print("Users oldder then 28:")
for row in rows: 
    print(f"ID: {row[0]}, Name: {row[1]} , Age: {row[2]}, City: {row[3]}") 

conn.close  

