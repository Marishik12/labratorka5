# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# print(connection)
# print(cur)
# connection.close()

# import sqlite3
# connection = sqlite3.connect("itstep_DB.s13", 5)
# cur = connection.cursor()
# cur.execute("CREATE TABLE first table (name TEXT);")
# connection.commit()
# connection.close()

# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first table (name) VALUES ('Nick');")
# connection.commit()
# connection.close()

# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("SELECT rowid, name FROM First-table")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()

# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()

# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=3;")
# connection.commit()

# import sqlite3
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("DELETE FROM first_table WHERE rowid=4;")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()