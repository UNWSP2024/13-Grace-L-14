'''Create Cities Database Program
By Grace LeVoir
5 - 1 - 26'''



import sqlite3


conn = sqlite3.connect('cities.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE cities (
                   CityID INTEGER PRIMARY KEY,
                    CityName TEXT,
                    Population REAL )''')

cities = [
    ('New York', 8335000),
    ('Los Angeles', 3822000),
    ('Chicago', 2665000),
    ('San Francisco', 864816),
    ('Houston', 2302000),
    ('San Diego', 1388000),
    ('Phoenix', 1650000),
    ('Philadelphia', 1550000),
    ('San Antonio', 1495000),
    ('Dallas', 1302000),
    ('Jacksonville', 985000),
    ('Austin', 931830),
    ('San Jose', 1026908),
    ('Fort Worth', 956000),
    ('Columbus', 907971),
    ('Charlotte', 897000),
    ('Indianapolis', 853173),
    ('Seattle', 801192),
    ('Denver', 734718),
    ('Washington, D.C.', 717916)
]


cur.executemany('INSERT INTO cities (CityName, Population) VALUES (?,?)', cities)


'''Test database'''
# cur.execute("SELECT * FROM cities")
#
# rows = cur.fetchall()
#
# for row in rows:
#     print(row)


conn.commit()
conn.close()