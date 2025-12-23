# hash table for store books
library_catalog = {
    "978-5-389-07435-4": {
        "title": "The Master and Margarita",
        "author": "Mikhail Bulgakov",
        "year": 1966,
        "status": "available"
    },
    "978-5-17-090630-3": {
        "title": "Crime and Punishment",
        "author": "Fedor Dostoevsky",
        "year": 1866,
        "status": "checked_out"
    },
    "978-5-23-1867-8": {
        "title": "War and Peace",
        "author": "Fedor Dostoevsky",
        "year": 1867,
        "status": "available"
    }
}

#find a book by isbn
def find_book(isbn):
    book_info = library_catalog.get(isbn)
    if book_info:
        return print(book_info)
    else:
        return print("The book was not found.")

book = find_book("978-5-23-1867-8")

#adding a book for catalog
def add_new_book(isbn, title, author, year, status):
    library_catalog[isbn] = {
        "title": title,
        "author": author,
        "year": year,
        "status": status
    }
    print(f"The book {title} has been added to the catalog")

add_new_book('jxx-bsjbsjbs-jsb4sbsb2','SilverGoldi',"67",2025,'available')

