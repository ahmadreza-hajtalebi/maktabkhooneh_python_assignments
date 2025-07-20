from mylibrary.library import LIBRARY

if __name__ == "__main__":
    l = LIBRARY()
    l.add_book("math", "alamdari")
    l.show_books()
    l.search_book("math")
    l.remove_book("math")
    l.show_books()
else :
    print("please use from original imported file")