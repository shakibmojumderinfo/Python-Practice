# friends = ["shomun" , "shakib" , "rakib" , "shawon"]

# start_s = []

# for friend in friends:
#     if friend.startswith("s"):

#         start_s.append(friend)
#     print(friend)

#     print("and here is startwith s friend ")
        

# print(start_s)



# frnd = ["masum" , "nadia" , "morium"]

# start_m = []

# for friend in frnd:
#     if friend.startswith("m"):

#         start_m.append(frnd)
#         print(friend)

# print("here your name starts with s")

# print(start_m)

# import numpy as np
# import matplotlib.pyplot as plt

# # Create a NumPy array of dots
# dots = np.random.rand(100, 2) * 100

# # Create a figure and axes
# fig, ax = plt.subplots()

# # Plot the dots
# ax.scatter(dots[:, 0], dots[:, 1], s=10, c='black')

# # Set the axes limits
# ax.set_xlim(-100, 100)
# ax.set_ylim(-100, 100)

# # Set the aspect ratio to equal
# ax.set_aspect('equal')

# # Turn off the axes labels
# ax.set_xlabel('')
# ax.set_ylabel('')

# # Create an animation
# def animate(i):
#     # Update the position of the dots
#     dots[:, 0] += i
#     dots[:, 1] += np.sin(i)

#     # Plot the dots
#     ax.clear()
#     ax.scatter(dots[:, 0], dots[:, 1], s=10, c='black')

# ani = plt.animation.FuncAnimation(fig, animate, interval=10)

# # Show the animation
# plt.show()


from PIL import Image

# Create a new image
img = Image.new('L', (200, 200), 0)

# Draw two gray squares
img.rectangle([(50, 50), (150, 150)], fill=128)
img.rectangle([(150, 50), (250, 150)], fill=128)

# Add some horizontal lines to the left square
for i in range(50, 150, 10):
    img.line([(50, i), (150, i)], fill=255)

# Save the image
img.save('illusion.png')

