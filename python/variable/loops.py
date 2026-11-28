# For Loop
students = ["Jyoshna", "Hemanth", "Rahul", "Priya", "Arjun"]
for name in students:
    if name == "Rahul":
        continue
    if name == "Priya":
        break
    print("Present:", name)
print("Attendance completed")

# While Loop
items = ["Shirt", "Shoes", "Watch", "Bag"]
index = 0
while index < len(items):
    item = items[index]
    if item == "Watch":
        break
    print("Shopping Item:", item)
    index += 1
print("Shopping completed")