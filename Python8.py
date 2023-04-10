#L
width = 7
height = 7

for row in range(height):
    for column in range(width):
        if row == column or row + column == height - 1:
            print("X", end="")
        else:
            print(" ", end="")
    print()