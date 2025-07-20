class LIBRARY():
    books = {}
    def add_book(self, title, author):
        LIBRARY.books [title] = author
        print(f"{title} by {author} successfully added to book")
    def remove_book(self, title):
        if title in LIBRARY.books:
            del LIBRARY.books[title]
            print(f"{title} successfully removed of book")
        else:
            print("your book is not available")
    def search_book(self, title):
        if title in LIBRARY.books:
            return LIBRARY.books[title]
        else:
            print("your book is not available")
            return None
    def show_books(self):
        if not LIBRARY.books:
            print("list is empty")
            return None
        else:
            print(f"{LIBRARY.books}")