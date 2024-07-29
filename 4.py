class LibraryManager:
    def __init__(self):
        self.books = {}
        
    def add_book(self, isbn, title, author, publisher, volume, year, isbn_num):
        if isbn in self.books:
            return "Book with this ISBN already exists."
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year,
            "isbn": isbn_num
        }
        return "Book added successfully."
    
    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            return "Book removed successfully."
        return "Book not found."
    
    def get_book(self, isbn):
        if isbn in self.books:
            return self.books[isbn]
        return "Book not found."
    
    def search_books(self, search_term, by="title"):
        results = []
        for book in self.books.values():
            if search_term.lower() in book[by].lower():
                results.append(book)
        return results
    
    def list_books(self):
        return list(self.books.values())
    
    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None, isbn_num=None):
        if isbn in self.books:
            if title:
                self.books[isbn]['title'] = title
            if author:
                self.books[isbn]['author'] = author
            if publisher:
                self.books[isbn]['publisher'] = publisher
            if volume:
                self.books[isbn]['volume'] = volume
            if year:
                self.books[isbn]['year'] = year
            if isbn_num:
                self.books[isbn]['isbn'] = isbn_num
            return "Book updated successfully."
        return "Book not found."
    
    def check_availability(self, isbn):
        return isbn in self.books


def main():
    lib_manager = LibraryManager()
    
    while True:
        print("\nLibrary Manager")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Retrieve Book Details")
        print("4. Search Books")
        print("5. List All Books")
        print("6. Update Book Details")
        print("7. Check Book Availability")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            publisher = input("Enter Publisher: ")
            volume = input("Enter Volume: ")
            year = input("Enter Year: ")
            isbn_num = input("Enter ISBN Number: ")
            print(lib_manager.add_book(isbn, title, author, publisher, volume, year, isbn_num))
            
        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            print(lib_manager.remove_book(isbn))
            
        elif choice == '3':
            isbn = input("Enter ISBN of the book to retrieve: ")
            print(lib_manager.get_book(isbn))
            
        elif choice == '4':
            search_term = input("Enter search term: ")
            by = input("Search by (title/author): ")
            results = lib_manager.search_books(search_term, by)
            for book in results:
                print(book)
                
        elif choice == '5':
            books = lib_manager.list_books()
            for book in books:
                print(book)
                
        elif choice == '6':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new Title (leave blank to keep current): ")
            author = input("Enter new Author (leave blank to keep current): ")
            publisher = input("Enter new Publisher (leave blank to keep current): ")
            volume = input("Enter new Volume (leave blank to keep current): ")
            year = input("Enter new Year (leave blank to keep current): ")
            isbn_num = input("Enter new ISBN Number (leave blank to keep current): ")
            print(lib_manager.update_book(isbn, title, author, publisher, volume, year, isbn_num))
            
        elif choice == '7':
            isbn = input("Enter ISBN to check availability: ")
            print("Available" if lib_manager.check_availability(isbn) else "Not available")
            
        elif choice == '8':
            print("THNAK YOU!!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
