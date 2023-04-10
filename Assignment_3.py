#1+2
try:
    a = 1/0
except ZeroDivisionError:
    print("Division by zero is not allowed!")
#3. Is the following code legal?
try :
x = 1
finally :
print(“finally”)
#Yes

#4
# All types of exceptions

#5
# The Except needs to have a statement before the : about the error type and needs to have a try above it
# it can be used to clarify error codes and also make some changes

#6
except IOError:
# For errors on unable to read file
except ZeroDivisionError
# Foe errors on dividing  by zero

#7 + 8
file = open("words.txt", "w")
file.write("Text\n")
file.close()

#9
file = open("words.txt", "r")
print(file.read())
file.close()

#10
with open("words.txt", "w", encoding="utf-8") as file:
    file.write("היי.")
    file.close()
with open("words.txt", "r", encoding="utf-8") as file:
    contents = file.read()
    print(contents)
#11
from PIL import Image, ImageDraw

size = (2000, 2000)
color = (255, 255, 255)
image = Image.new(mode="RGB", size=size, color=color)

draw = ImageDraw.Draw(image)

x, y = size[0]//2, size[1]//2
r = min(x, y)//2
draw.rectangle((x-r, y-r, x+r, y+r), fill=(0, 0, 0))

image.save("red_square.png")
