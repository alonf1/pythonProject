names = ["Daniel", "Shai", "roei"]

names.append("shmulik")

if "shmulik" in names:
    sm = "Shmulik"
    print(sm + " is in the list")
else:
    print(names)

print(len(names))



d = 5
g = 5
f = [1, 2, 3]
h = [1, 2, 3]
if d is g:
    print("d is g")
if f is h:
    print("f is h")
if type(d) is int:
    print("d is int")