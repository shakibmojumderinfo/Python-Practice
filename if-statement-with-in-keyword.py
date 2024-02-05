# movie_list = {"less than" , "greater than" , "equal to"}
# moviewatch = input("Enter some movie you watchad : ")

# if moviewatch in movie_list:
#     print(f"I have watchad {moviewatch} to")

# else:
#     print("I dont watch this movie ")





num = 10

user_input = input("if you want play write 'y' : ")

if user_input == "y":
    user_number = int(input("Guess the number: "))
    if user_number == num:
        print("your guessed correctly")
    else:
        print("sorry its wrong")