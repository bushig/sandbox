import sqlite3
import random


con = sqlite3.connect('/home/bogdan/PycharmProjects/sandbox/test.db')

cur = con.cursor()


cur.execute('CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT , login VARCHAR(8))')
cur.execute('CREATE TABLE statistics(id INTEGER PRIMARY KEY AUTOINCREMENT, user INTEGER, number INTEGER, FOREIGN KEY(user) REFERENCES users(id))')

cur.execute('INSERT INTO users(login) VALUES ("bushig")')


for i in range(10000):
    numb= random.randint(1, 1000000)
    cur.execute('INSERT INTO statistics(user, number) VALUES(1, {})'.format(numb))

cur.execute('SELECT * FROM statistics')

students=cur.fetchall()

for stud in students:
    print(stud)

cur.close()

con.commit()
con.close()