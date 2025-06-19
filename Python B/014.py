import sqlite3 as sql

database = sql.connect("C:\\SQLite\\schooltest.db")
do = database.cursor()


def createTable():
    name = input("Enter the name of the table: ")
    columns = input("Enter the columns (comma separated): ")
    query = f"CREATE TABLE IF NOT EXISTS {name} ({columns})"
    do.execute(query)
    database.commit()
    print(f"Table '{name}' created successfully.")


def insetData():
    name = input("Enter the name of the table: ")
    columns = input("Enter the columns (comma separated): ")
    values = input("Enter the values (comma separated): ")
    try:
        query = f"INSERT INTO {name} ({columns}) VALUES ({values})"
        do.execute(query)
        database.commit()
        print(f"Data inserted into table '{name}' successfully.")
    except sql.Error as e:
        print(f"An error occurred: {e}")
        return


def ShowData():
    name = input("Enter the name of the table: ")
    query = f"SELECT * FROM {name}"
    try:
        do.execute(query)
        rows = do.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print(f"No data found in table '{name}'.")
    except sql.Error as e:
        print(f"An error occurred: {e}")
        return


def deleteData():
    name = input("Enter the name of the table: ")
    condition = input("Enter the condition for deletion (e.g., id=1): ")
    query = f"DELETE FROM {name} WHERE {condition}"
    try:
        do.execute(query)
        database.commit()
        print(f"Data deleted from table '{name}' successfully.")
    except sql.Error as e:
        print(f"An error occurred: {e}")
        return


def updateData():
    name = input("Enter the name of the table: ")
    set_values = input("Enter the values to update (e.g., column1=value1, column2=value2): ")
    condition = input("Enter the condition for updating (e.g., id=1): ")
    query = f"UPDATE {name} SET {set_values} WHERE {condition}"
    try:
        do.execute(query)
        database.commit()
        print(f"Data updated in table '{name}' successfully.")
    except sql.Error as e:
        print(f"An error occurred: {e}")
        return


def main():
    while True:
        print("\nMenu:")
        print("1. Create Table")
        print("2. Insert Data")
        print("3. Show Data")
        print("4. Delete Data")
        print("5. Update Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            createTable()
        elif choice == '2':
            insetData()
        elif choice == '3':
            ShowData()
        elif choice == '4':
            deleteData()
        elif choice == '5':
            updateData()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
