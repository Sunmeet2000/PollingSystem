import sqlite3

conn = sqlite3.connect('polling.db')
c = conn.cursor()
c.execute("""select * from user""")
#c.execute("""CREATE TABLE IF NOT EXISTS `user` ( `username` varchar(100) NOT NULL, `password` varchar(100) NOT NULL )""")
# #c.execute("""select * from g_list""")
# c.execute("""INSERT INTO user(username, password)
#                  VALUES("snmt", "1234")""")
conn.commit()
rows = c.fetchall()
print(rows)