from PIL import Image, ImageDraw

# Create a new image with white background
size = (2000, 2000)
color = (255, 255, 255)
image = Image.new(mode="RGB", size=size, color=color)

# Get a drawing context
draw = ImageDraw.Draw(image)

# Draw a red square in the center of the image
x, y = size[0]//2, size[1]//2
r = min(x, y)//2
draw.rectangle((x-r, y-r, x+r, y+r), fill=(0, 0, 0))

# Save the image as PNG
image.save("red_square.png")
