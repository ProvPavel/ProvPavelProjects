import sqlite3

data = open('times.db', 'r')
con = sqlite3.connect("times.db.sqlite")
cur = con.cursor()
a = int(input())
b = int(input())
another_time = {'events': list(set(cur.execute("""SELECT event FROM films""").fetchall())).sort(),
                'places': list(set(cur.execute("""SELECT place FROM films""").fetchall())).sort(),
                'total_danger': sum(list(cur.execute("""SELECT danger FROM films""").fetchall()))}
con.close()

