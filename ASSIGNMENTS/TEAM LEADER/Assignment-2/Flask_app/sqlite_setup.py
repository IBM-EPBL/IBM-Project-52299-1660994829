import sqlite3

conn=sqlite3.connect("student.db")

print("Success")

conn.execute("CREATE TABLE Info(name TEXT,pass TEXT)")

conn.close()

