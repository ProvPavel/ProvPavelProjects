import sqlite3


def tag_choice(teg, captain):
    result = open('to_tell.csv', 'a')
    con = sqlite3.connect('incidents.db')
    cur = con.cursor()
    a = cur.execute('''SELECT event FROM Cases WHERE captain == ? and genre = (
                            SELECT id FROM genres
                            WHERE title = 'фантастика')''').fetchall()
    con.close()
