# class Student:
    
#     def __init__(self, name, age):
        
#         self.name = name
#         self.age = age
#         print("My name is shakib. I'm 30 years old")
        
# s1=Student("Shakib", 20)
# s2=Student("Shawon", 22)
# print(s1.name)
# s1.age=30
# print(s1.age)


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def  avarege_grades(self):
        return sum(self.grades) / len(self.grades)
    
student1 = Student("Shakib", (100, 23, 67,  87, 78))
student2 = Student("Shawon", (79, 34, 78,  65, 97, 56))

print(student1.name)
print(student1.avarege_grades())

print(student2.name)
print(student1.avarege_grades())

