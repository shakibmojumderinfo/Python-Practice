# squars = [ x for x in range (1,11) if x % 3 ==0]
# print(squars)


friends = ["shakib", "rakib", "nitu", "tamanna" ,"sneha", "niha", "shobon", "sohel"]
start_s = [friend for friend in friends if friend.startswith("s")]

# for friend in friends:
#     if friend.startswith("s"):
#         start_s.append(friend)

print(start_s)
