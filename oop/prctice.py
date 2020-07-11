class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return "Repr"

    def __str__(self):
        return "Uni"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("The book has been deleted")


book = Book("Joe", "James Joyce", 100)

print(str(book))
print(len(book))
del(book)
book