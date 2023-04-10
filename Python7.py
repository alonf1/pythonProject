# 1. input for 5 ages from the user
#  print out the biggest age from the user
# 2. write a function the get name as input
# from the user until the name 'moshe' and return a list of those names

age = []
left = 5
for i in range(left):
    age.append(int(input(f"Enter your age ({left-i} left): ")))
largest_age = max(age)
print(largest_age)
print(age)
