# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
        
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
        
#     @staticmethod
#     def static_method():
#         print("Called static_method: ")
        
# ClassTest.static_method()

class Book:
    Types = ("hardcover", "paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<book name : {self.name}, Book Type : {self.book_type}, and Book Weight : {self.weight}> "

    @classmethod
    def book_type(cls, name, page_weight):
        return Book(name, Book.Types[1], page_weight + 300)

book = Book.book_type("Harry Potter", 500)
# book = Book(name="Harry Potter", book_type="Comic book" , weight=500)
print(book)