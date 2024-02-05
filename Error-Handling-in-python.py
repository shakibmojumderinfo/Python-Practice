# def divide(dividend, divisor):
#     return dividend / divisor
# students = [
#     {"name": "Shakib", "grades" : [76, 88, 87]},
#     {"name": "Rahim", "grades" : []},
#     {"name": "Korim", "grades" : [87, 99, 89]},
    
# ]

# try:
#     for student in students:
        
#         name = student["name"]
#         grades = student["grades"]
        
#         # if I want korim grades avarage also 
#         if len(grades) == 0:
#             continue
        
#         average = divide(sum(grades), len(grades))
            
#         print(f"{name} averaged {average}.")
        
# except ZeroDivisionError:
#     print(f"ERROR: {name} has no grades!")

# else:
#     print("-- All student averages calculated --")

# finally:
#     print("--End fo student average calculated")



def divide(dividend, divisor):
    return dividend / divisor
students = [
    {"name": "Shakib", "grades" : [76, 88, 87]},
    {"name": "Rahim", "grades" : [77,88]},
    {"name": "Korim", "grades" : [87, 99, 89]},
    
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    
    avarege = divide(sum(grades), len(grades))
    print(f"{name}, {avarege}")