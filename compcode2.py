#PYTHON CODE
'''Build a simple command-line based library management system that
allows users to manage books and members using basic Create, Read,
Update, Delete operations directly within the application'''

import csv
import os

BOOKS_FILE = "books.csv"
MEMBERS_FILE = "members.csv"

def initialize_csv(file, headers):
    if not os.path.exists(file):
        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    with open(BOOKS_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([book_id, title, author])
    print("Book added successfully!\n")

def view_books():
    with open(BOOKS_FILE, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    rows = []
    with open(BOOKS_FILE, mode='r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != book_id]
    with open(BOOKS_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Book deleted successfully!\n")

def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    with open(MEMBERS_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([member_id, name])
    print("Member added successfully!\n")

def view_members():
    with open(MEMBERS_FILE, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def delete_member():
    member_id = input("Enter Member ID to delete: ")
    rows = []
    with open(MEMBERS_FILE, mode='r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != member_id]
    with open(MEMBERS_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Member deleted successfully!\n")

def main():
    initialize_csv(BOOKS_FILE, ["Book ID", "Title", "Author"])
    initialize_csv(MEMBERS_FILE, ["Member ID", "Name"])
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Add Member")
        print("5. View Members")
        print("6. Delete Member")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            add_member()
        elif choice == '5':
            view_members()
        elif choice == '6':
            delete_member()
        elif choice == '7':
            print("Exiting...\n")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

