class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    # def __str__(self):
    #     return f"My name is {self.name}, I'm {self.age} years old"
        
    def __repr__(self):
        return f"<My name is {self.name}, I'm {self.age} years old>"
    

person = Person(name="bob", age=30)  
print(person)
