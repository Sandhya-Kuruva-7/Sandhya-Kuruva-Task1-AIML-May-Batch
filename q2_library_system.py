def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)

def register_member(members, member_id):
    members.add(member_id)

def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"{book_id}: {title} by {author} ({year})")


def main():
    catalog = {}            
    borrowed_books = []     
    members = set()       

    # Add 4 books
    add_book(catalog, 101, "Python Basics", "Guido", 2010)
    add_book(catalog, 102, "Data Structures", "Mark", 2015)
    add_book(catalog, 103, "Algorithms", "Thomas", 2018)
    add_book(catalog, 104, "AI Intro", "Andrew", 2020)

    # Register 3 members
    register_member(members, 501)
    register_member(members, 502)
    register_member(members, 503)
    register_member(members, 502)   

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Return 1 book
    return_book(borrowed_books, 101)

    # final available books
    show_available(catalog, borrowed_books)

main()