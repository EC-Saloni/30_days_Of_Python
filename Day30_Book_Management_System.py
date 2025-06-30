#Day_30 
""" Final Capstone Project - Book Management System
- Add, update, delete books
- Search by author or title
- Save data in file (CSV or JSON)"""

import json
import os

DATA_FILE ="books.json"

#Load Data
def load_books():
    print(os.path.exists(DATA_FILE))
    print(DATA_FILE)
    if not os.path.exists(DATA_FILE):
        return[]
    with open(DATA_FILE, "r") as file:
        return json.load(file)

#Save data
def save_books(books):
    with open (DATA_FILE,"w")as file:
        json.dump(books,file,indent=4)

#Add books
def add_book(books):
    title = input("Enter title of the book:")
    author =input("Enter the name of the author of book:")
    year = input("Enter the year of book published:")
    book_id = max((book.get("id", 0) for book in books), default=0) + 1

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "year": year
    })
    print("✅ Book updated successfully! ")

#Update a book
def update_book(books):
    book_id = int(input("Enter the book ID to update: "))
    for book in books:
        if book["id"]== book_id:
            book["title"]=input("New title :")
            book["author"]= input("New author :")
            book["year"] = input("New Year :")
            print("✅ Updated Successfully !")
            return
    print("❌ Book not found.")
            
#Delete a book
def delete_book(books):
    book_id = int(input("Enter the book Id to delete:"))
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("✅Book Deleted Successfully !")
            return
    print("❌ Book is not found")

#Search books
def search_books(books):
    keyword = input("Enter the title or author to search :").lower()
    found =[b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower() ]
    if found:
        for b in found:
            print(f"{b['id']} : {b['title']} by {b['author']} in {b['year']}")
    else:
        print("❌No matching book found")

#Show Menu
def main():
    print("start")
    books = load_books()
    while True:
        print("\n-----Book Managenment Menu-----")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Books")
        print("5. Show all Books")
        print("6. Exit")

        choice = input("Enter Your Choice (1-6):")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_book(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            search_books(books)
        elif choice == '5':
            for b in books:
                print(f"{b['id']} : {b['title']} by {b['author']} {b['year']}")
        elif choice == '6':
            save_books(books)
            print("📁 Data saved. Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()