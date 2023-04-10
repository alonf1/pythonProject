names = ["inbar", "lanir", "kfir", "alina"]

numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    if number == 3:
        continue

    if number == 2:
        break
    print(number)
else:
    print ("finished successfully")

a = 0
while a < 5:
    print(a)
    a += 1
else:
    print("finished")
    