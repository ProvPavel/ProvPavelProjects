import sqlite3

con = sqlite3.connect('times.db')
cur = con.cursor()
a = int(input())
b = int(input())
another_time = {'events': sorted(list(map(lambda v: v[0],
                                          list(set(cur.execute("""SELECT event FROM Events
                                                        WHERE year BETWEEN ? and ?""",
                                                               (a, b)).fetchall()))))),
                'places': sorted(list(map(lambda v: v[0],
                                          list(set(cur.execute("""SELECT place FROM Events
                                                        WHERE year >= ? and year <= ?""",
                                                               (a, b)).fetchall()))))),
                'total_danger': sum(int(x[0]) for x in cur.execute("""SELECT danger FROM Events
                                        WHERE year >= ? and year <= ?""",
                                                                   (a, b)).fetchall())}
con.close()
print(another_time)
