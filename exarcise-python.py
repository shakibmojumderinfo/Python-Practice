# first = input("first : ")
# second = input("second : ")


# sum = int(first) + int(second)

# print(sum)

# first = input("first: ")
# second = input("second: ")
# sum = int(first) + int(second)

# print(sum)
# if sum == 1000:
#     for num in sum:

#         print(sum)


# temparature = 30

# if temparature == 31:
#     print("It's hot day")

# elif temparature > 10:
#     print("its intersting day ")

# elif temparature < 10:
#     print("have a bad day ")

# elif temparature == 30:
#     print("have a good day ")

# elif temparature <= 10:
#     print("bad temp")

# elif temparature <= 10:
#     print("nice day ")

# else:
#     print("Drink water")

# print("done")


# weight = int(input("Weight : "))

# unit = input("(K)g or (L)bs: ")

# if unit.upper() == "K" :
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))

# else:
#     converted = weight * 0.45
#     print("Weight in kgs: " + str(converted))



# ab = 12

# def abc(x, y=ab):
#     sum = (x + y)
#     print(sum)
# # if you even give the value x=3 if you write only 3 so its right its just 
# # give for reading code properly 
# abc(x=3)


# numbers = [10, 20, 30, 40, 50]

# new_numbers = list(map(lambda x: x / 2, numbers))

# print(new_numbers)


# number = [10, 20, 30, 40, 50]

# new_numbers = list(map(lambda x: x/2, number))

# # for numbers in new_numbers:

# #     print(numbers)

# print(new_numbers)

# while True:

#   first = input("first : ")
#   second = input("second : ")
#   third = input("third: ")
#   fourth = input("fourth : ")
#   fifth = input("fifth: ")
  

#   sum = int(first) + int(second) + int(third) + int(fourth) + int(fifth)
#   print(sum)


# users= [
#     (0, "shakib", "password"),
#     (1, "rakib", "rakib555"),
#     (2, "shimol", "fhfhfhf"),
#     (3, "nitu", "34344")
# ]

# username_mapping = {user[1]: user for user in users}

# username_input = input("enter your username: ")
# user_password = input("enter your password: ")

# _,username,password = username_mapping(username_input)

# if user_password == password:
#     print("your details are correct")

# else:
#     print("your details are incorrect")

users = [
    (0, "shakib", "password"),
    (1, "rakib", "rakib555"),
    (2, "shimol", "fhfhfhf"),
    (3, "nitu", "34344"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
user_password = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if user_password == password:
    print("Your details are correct")
else:
    print("Your details are incorrect")





        
    









