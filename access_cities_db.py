'''Access Cities Database Program
By Grace LeVoir
5 - 1 - 26'''


import sqlite3

conn = sqlite3.connect('cities.db')
cur = conn.cursor()

cur.execute("SELECT CityName, Population FROM cities")

rows = cur.fetchall()

for name, population in rows:
    print(name + ": " + format(population))

conn.close()