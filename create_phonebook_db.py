'''Create Phonebook Database Program
By Grace LeVoir
5 - 1 - 26'''



import sqlite3


conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE Entries (
                   EntryID INTEGER PRIMARY KEY,
                    EntryName TEXT,
                    PhoneNumber REAL )''')


phonebook = [
    ('Lilly Lane', 166111222),
    ('Suzie Smith', 167111222),
    ('Bobby Brown', 168111222),
    ('Patty Peterson', 169111222),
    ('Makayla Mae', 170111222)
]


cur.executemany('INSERT INTO Entries (EntryName, PhoneNumber) VALUES (?,?)', phonebook)



'''Test'''
# cur.execute("SELECT * FROM Entries")
#
# rows = cur.fetchall()
#
# for row in rows:
#     print(row)


conn.commit()
conn.close()