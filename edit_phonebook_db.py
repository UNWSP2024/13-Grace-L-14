'''Edit Phonebook Database Program
By Grace LeVoir
5 - 1 - 26'''


import sqlite3

conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

def show_entries():
    cur.execute("SELECT * FROM Entries")
    for row in cur:
        print(row)

def insert_entries():
    name = input("Enter name: ")
    phone_no = input("Enter phone number: ")

    cur.execute("INSERT INTO Entries (EntryName, PhoneNumber) VALUES (?,?)", (name, phone_no))
    conn.commit()
    print("Entry added!")

def update_entries():
    show_entries()
    entry_id = input("Enter entry ID to update: ")

    updated_name = input("Enter updated name: ")
    updated_phone_no = input("Enter updated phone number: ")

    cur.execute("UPDATE Entries SET EntryName = ?, PhoneNumber = ? WHERE EntryID = ?", (updated_name, updated_phone_no, entry_id))
    conn.commit()
    print("Entry updated!")

def delete_entries():
    show_entries()
    entry_id = input("Enter entry ID to delete: ")

    cur.execute("DELETE FROM Entries WHERE EntryID = ?", (entry_id,))
    conn.commit()
    print("Entry deleted!")


while True:
    print("Welcome to the Phonebook Database!")
    print("1. View entries")
    print("2. Add entries")
    print("3. Update entries")
    print("4. Delete entries")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_entries()
    elif choice == 2:
        insert_entries()
    elif choice == 3:
        update_entries()
    elif choice == 4:
        delete_entries()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")

conn.close()