# def test1(func):
    
#     def exect():
        
        
#         print("Hi I'm Shakib Mojumder")
#         func()
#         print("I'm 16 years old")
#     return exect

# @test1
# def my_func():
#     print("Messi is better than Ronaldo")
    
# my_func()

# def test1(func):
    
#     def exect():
        
#         print("Hi I'm Shakib Mojumder")
#     func()
#     print("I'm 16 years old")
#     return exect

# @test1
# def my_func():
    
#     print("Messi is better than Ronaldo")

# my_func()
# List
my_list = [1, 2, 3, 4, 5]

# Dictionary
my_dict = {"name": "Shakib", "age": 16}

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Append
my_list.append(6)

# Loop
for item in my_list:
  print(item)

# If/else/elif statement
if my_age > 18:
  print("You are an adult.")
elif my_age > 13:
  print("You are a teenager.")
else:
  print("You are a child.")

# Booleans
my_bool = True
another_bool = False

# Operator
my_sum = 1 + 2
my_product = 1 * 2

# Keyword arguments
def my_func(name, age):
  print(f"Hello {name}, you are {age} years old.")

my_func(name="Shakib", age=16)

# Positional arguments
def my_func(a, b):
  print(f"The sum of {a} and {b} is {a + b}.")

my_func(1, 2)

# Lambda function
my_lambda = lambda a, b: a + b

print(my_lambda(1, 2))

# Set
my_set = {1, 2, 3, 4, 5}

# Data types
my_int = 1
my_float = 1.0
my_string = "Hello, world!"

# OOP
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name}.")

person = Person("Shakib", 16)
person.greet()

# Attribute
person.name = "Shakib Mojumder"

# Method
person.greet()

# __str__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"My name is {self.name} and I am {self.age} years old."

person = Person("Shakib", 16)
print(person)

# __repr__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f"Person(name='{self.name}', age={self.age})"

person = Person("Shakib", 16)
print(repr(person))

# Decorators
def my_decorator(func):
  def wrapper(*args, **kwargs):
    print("Before function call")
    func(*args, **kwargs)
    print("After function call")
  return wrapper

@my_decorator
def my_func():
  print("Hello from my_func!")

my_func()

# Error handling
try:
  1 / 0
except ZeroDivisionError:
  print("Division by zero is not allowed.")

