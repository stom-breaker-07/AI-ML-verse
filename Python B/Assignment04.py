# Book Store Managment with Data-Base

import sqlite3

db = sqlite3.connect("C:\\SQLite\\Bookstore.db")
do = db.cursor()


def insertData():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Book Price: "))
    try:
        do.execute("INSERT INTO Books (id, title, author, price) VALUES (?, ?, ?, ?)", (book_id, title, author, price))
        db.commit()
        print("Book-data inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


def enquiry_Book():
    name = input("Enter the name of the book :")
    try:
        do.execute("SELECT * FROM Books WHERE title = ?", (name,))
        rows = do.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


def delete_Book():
    book_name = input("Enter the Book Title to delete: ")
    try:
        do.execute("DELETE FROM Books WHERE title= ?", (book_name,))
        db.commit()
        if do.rowcount > 0:
            print("Book deleted successfully.")
        else:
            print("No book found with that title.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


def update_Book():
    update_name = input("Enter the name of the book to update: ")
    new_val = input("Enter your update value (eg title=new_value,author=new_value,price=new_value): ")
    try:
        do.execute(f"UPDATE Books SET {new_val} WHERE title = ?", (update_name,))
        db.commit()
        if do.rowcount > 0:
            print("Book updated successfully.")
        else:
            print("No book found with that title.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


def Show_Books():
    try:
        do.execute("SELECT * FROM Books")
        rows = do.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No books found in the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


def Billing(title, quantity):
    try:
        do.execute("SELECT price FROM Books WHERE title = ?", (title,))
        row = do.fetchone()
        if row:
            price = row[0]
            total_amount = price * quantity
            print(f"Total amount for {quantity} copies of '{title}': ${total_amount:.2f}")
        else:
            print("Book not found.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


def main():
    while True:
        print("\nBookstore Management System")
        print("1. Insert Book Data")
        print("2. Enquire Book")
        print("3. Delete Book")
        print("4. Update Book")
        print("5. Show All Books")
        print("6. Billing")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insertData()
        elif choice == '2':
            enquiry_Book()
        elif choice == '3':
            delete_Book()
        elif choice == '4':
            update_Book()
        elif choice == '5':
            Show_Books()
        elif choice == '6':
            title = input("Enter the book title for billing: ")
            quantity = int(input("Enter the quantity: "))
            Billing(title, quantity)
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
    db.close()  # Close the database connection when done
