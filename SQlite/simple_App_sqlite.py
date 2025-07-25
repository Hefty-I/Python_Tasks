import sqlite3

conn = sqlite3.connect("Students.db")
cursor = conn.cursor()

cursor.execute(
    """
               create table if not exists Students(
               id integer primary key autoincrement,
               name text,
               gender text,
               age integer,
               phone integer,
               email text)"""
)
conn.commit()


def add_info():
    name = input("Enter name: ")
    gender = input("Enter gender (M/F): ")
    age = int(input("Enter your age: "))
    phone = int(input("Enter your phone number: "))
    email = input("Enter your email: ")

    cursor.execute(
        "insert into Students (name, gender, age, phone, email) values (?,?,?,?,?)",
        (name, gender, age, phone, email),
    )
    conn.commit()

    print("👍 Information Added \n")


def display():
    cursor.execute("select * from Students")
    data = cursor.fetchall()

    for i in data:
        print(
            f"\n ID: {i[0]}, Name: {i[1]}, Gender: {i[2]}, Age: {i[3]}, Phone #: {i[4]}, Email: {i[5]} \n"
        )


def search_contact():
    id = int(input("Enter the id whose info you want to get : "))
    cursor.execute("select * from Students where id = ?", (id,))
    data = cursor.fetchall()
    if data:
        for i in data:
            print(
                f"\nID: {i[0]}, Name: {i[1]}, Gender: {i[2]}, Age: {i[3]}, Phone #: {i[4]}, Email: {i[5]}"
            )
    else:
        print("No contact found.")
    print()  # for newline after printing the result


def update_info():
    id = int(input("Enter the id whose info you want to update : "))
    cursor.execute("select * from Students where id = ?", (id,))
    data = cursor.fetchone()
    if data:
        name = input("Enter new name: ")
        gender = input("Enter new gender (M/F): ")
        age = int(input("Enter new age: "))
        phone = int(input("Enter new phone number: "))
        email = input("Enter new email: ")

        cursor.execute(
            "update Students set name = ?, gender = ?, age = ?, phone = ?, email = ? where id = ?",
            (name, gender, age, phone, email, id),
        )
        conn.commit()
        print("👍 Information Updated \n")
    else:
        print("No contact found.")

def delete_info():
    id = int(input("Enter the id of the contact you want to delete: "))
    cursor.execute("select * from Students where id = ?", (id,))
    data = cursor.fetchone()
    if data:
        cursor.execute("delete from Students where id = ?", (id,))
        conn.commit()
        print("Contact deleted successfully.")
    else:
        print("No contact found.")

# Menu
while True:
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact by Name")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_info()
    elif choice == "2":
        display()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_info()
    elif choice == "5":
        delete_info()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")

# Close the connection when done
conn.close()
