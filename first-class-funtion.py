# from operator import itemgetter

# def search(sequence, expected, finder):
#     for elem in sequence:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f"Could not find an element with {expected}.")
    
    
# friends = [
#     {"name": "Shakib Mojumder", "age": 34},
#     {"name": "Rohim", "age": 22},
#     {"name": "Leo Messi", "age": 34, "World Cup": 1},
#     {"name": "CR7", "age": 38, "World Cup": 2}
# ]

# print(search(friends, "Leo Messi", itemgetter(("name")) ))

# a = [1,2,3,4,5,6,7,8,9]
# a.reverse()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(a) // 2):
    
#     a[i], a[-i - 1] = a[-i - 1], a[i]

# print(a)