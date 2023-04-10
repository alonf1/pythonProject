#A
a = 4
b = 5

if a > b:
    print ("BIG")
elif a < b:
    print ("Small")
else:
    print("Error")
#B
for x in range(5):
    print(x)

#C

weather = 1

if weather == 1:
    print("summer")
elif weather == 2:
    print("winter")
elif weather == 3:
    print("fall")
elif weather == 4:
    print("spring")
else:
    print("Error")
#D
count = 1
while count <11:
    print(count)
    count += 1
# 10

#E
age = 28
letter = "F"
currency = 9.21
Flight = True
apartment = 493

print(age)
print(letter)
print(currency)
print(Flight)
print(apartment)
print(currency+age)

#F
number = input ("What is your phone number? ")
print(f"your phone number is {number}")

#G.1
def helloprint():
    print("Hello ")
helloprint()
#G.2
def calculate_add(a, b):
    result = a + b
    return result
number = calculate_add(5, 3.2)
print(number)

#H.1
def nameprint():
    name = input("What is your name? ")
    print(name)
nameprint()
#H.2
def calculate_div(a, b):
    result = a / b
    return result
number = calculate_div(100, 10)
print(number)

#I.1
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_numbers(3, 4)
print(result)

#I.2
def add_space(str1, str2):
    spaced_str = str1 + " " + str2
    return spaced_str

result = add_space("Alon", "Falah")
print(result)

#K
height = 5

for row in range(height):
    for column in range(row + 1):
        print("#", end="")
    print()
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

#M

def numinput():
    number_str = input("Enter number: ")
    number = float(number_str)
    return number

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    digit_sum = sum(digits)
    return digit_sum


result = numinput()
print("You entered:", result)
digit_sum = sum_digits(int(result))
print("The sum of the digits of", result, "is", digit_sum)


