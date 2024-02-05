# def user_age_in_second():
#     user_age = int(input("Enter your age: "))
#     age_second = user_age * 365 * 24 * 60*60
#     print(f"your age is second is {age_second}.")

# print("Wellcome to our age in second programm")

# user_age_in_second()

# print("Thank you. See you again")

def grade(n):
    if n >= 100:
        return 'A+'
    elif n >= 80:
        return 'A'
    elif n >= 70:
        return 'A-'
    elif n >= 60:
        return 'C'
    elif n>=50 :
        return 'D'
    else:
        return "F"
    

n = int(input("Enter your Number : "))
print(grade(n))

# while True:
#     def user_age_in_second():
#         user_age = int(input("Enter your age: "))
#         age_in_second = user_age * 356*24*60*60
#         print(f"your age is second is {age_in_second}.")

#     print("Wellcome to our new program")

#     user_age_in_second()
#     print("Thank you")
    
    
# while True:
#     def user_age_second():
        
#         age = int(input("Enter your age :"))
#         age_in_second = age*365*24*60*60
        
#         print(f"you age in second is {age_in_second}")
#     print("wellcome to our new programm")

#     user_age_second()

#     print("thank you")



# একটি def ব্লকটি একটি নতুন ফাংশন সংজ্ঞায়িত করে।
# ফাংশনটির নাম হল reverse_number এবং এটি একটি প্যারামিটার n গ্রহণ করে।
# def reverse_number(n):
    
# # reversed_number একটি ভেরিয়েবল যা ফাংশনটি 
# # চালানোর সময় বিপরীত সংখ্যাটি সংরক্ষণ করবে। 
# # এটিকে প্রথমে 0-তে সেট করা হয়েছে।
#     reversed_number = 0
    
# # একটি while লুপটি ফাংশনটি চালানোর সময় n > 0 পর্যন্ত চলবে।
#     while n > 0:
        
# # remainder ভেরিয়েবলটি n এর 10 দিয়ে ভাগ করার অবশিষ্ট অংশটি সংরক্ষণ করবে।
#         remainder = n % 10
        
# # reversed_number ভেরিয়েবলটিতে 
# # remainder যোগ করে বিপরীত সংখ্যাটি তৈরি করা হয়।
#         reversed_number = reversed_number * 10 + remainder
        
# # n ভেরিয়েবলটি n / 10 দ্বারা ভাগ করে n এর মানটি একক সংখ্যায় হ্রাস করা হয়।
#         n = n // 10
        
# # return বিবৃতি ফাংশনটি শেষ করে এবং reversed_number 
# # ভেরিয়েবলের মানটি ফাংশনটিকে কলকারী কোডের কাছে ফেরত দেয়।
#     return reversed_number

# # number ভেরিয়েবলটি 123456789 সংখ্যাটিকে সংরক্ষণ করে।
# number = 123456789
    
# # reversed_number ভেরিয়েবলটিতে reverse_number() 
# # ফাংশনটিকে number ভেরিয়েবলের সাথে কল করার ফলাফলটি সংরক্ষণ করা হয়।
# reversed_number = reverse_number(number)

# # f-string ব্যবহার করে reversed_number
# # ভেরিয়েবলের মান সহ একটি বার্তা মুদ্রণ করা হয়।
# print(f"The reversed number of {number} is {reversed_number}")


def reverse_number(n):
    reverse_number = 0
    
    while n > 0 :
        remain = n % 10
        reverse_number = reverse_number*10 + remain
        n = n // 10
        
    return reverse_number
    
number = 1234567891
reverse_number = reverse_number(number)

print(f"The reverse number of {number} is {reverse_number}")
        




# while True:
#     def user_age_second():
#         user_age = int(input("Enter your age: "))
#         age_second = user_age * 365 * 24 * 60*60
#         print(f"Your age in second is {user_age}")

#     def age_in_second():
#         user_age = int(input("Enter your age: "))
#         age_second = user_age * 365 * 24 * 60*60
#         print(f"Your age in second {age_second}.")

#     age_in_second()



# friends = []

# def friend():
#     friends.append("shakib")


# friend()
# friend()


# print(friends)


# # Function arguments and parameters

# def gym(a,b):
#     result = a+b
#     print(result)

# gym(2,3)


# def say_hello(name, age, strandard):
#     print(f"Hi i'm, {name} I'm  {age} years old, I read in {strandard} strandard")
    

# say_hello(name="shakib", age=12 , strandard="Ten")
# say_hello(age="rakib", name=14, strandard="Eleben")










# import os
# import glob

# def main():
#     # ফোল্ডার থেকে সমস্ত ফাইল পান
#     files = glob.glob("*.mp3") + glob.glob("*.mp4")

#     # ফাইলগুলিকে তাদের ফর্ম্যাট অনুসারে আলাদা করুন
#     mp3_files = [f for f in files if f.endswith(".mp3")]
#     mp4_files = [f for f in files if f.endswith(".mp4")]

#     # MP3 ফাইলগুলিকে একটি নতুন ফোল্ডারে রাখুন
#     if mp3_files:
#         os.makedirs("mp3", exist_ok=True)
#         for f in mp3_files:
#             os.rename(f, os.path.join("mp3", os.path.basename(f)))

#     # MP4 ফাইলগুলিকে একটি নতুন ফোল্ডারে রাখুন
#     if mp4_files:
#         os.makedirs("mp4", exist_ok=True)
#         for f in mp4_files:
#             os.rename(f, os.path.join("mp4", os.path.basename(f)))

# if __name__ == "__main__":
#     main()
