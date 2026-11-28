# List
student_names = ["Jyoshna", "Hemanth", "Rahul", "Priya", "Arjun"]
print(student_names[1])
# Slicing
print(student_names[1:4])
print(student_names[:3])
print(student_names[::2])
print(student_names[::-1])
# Useful methods
print(len(student_names))                    
print(student_names.count("Jyoshna"))       
print(student_names.index("Rahul"))          
student_names.sort()                         
print(student_names)
student_names.reverse()                      
print(student_names)


# Tuple
colors = ("red", "blue", "green", "red", "yellow")
# Access elements
print(colors[1])
# Slicing
print(colors[1:4])
print(colors[:3])
print(colors[::2])
print(colors[::-1])
# Useful methods
print(len(colors))             
print(colors.count("red"))     
print(colors.index("green"))   


# Set
numbers = {10, 20, 30, 10, 40, 50}
# Print set
print(numbers)
# Useful methods
print(len(numbers))       
numbers2 = numbers.copy() 
print(numbers2)

#dict
students = {
    "student1": {
        "name": "Jyoshna",
        "age": 19,
        "course": "Engineering"
    },
    "student2": {
        "name": "brundha",
        "age": 20,
        "course": "Computer Science"
    }
}

print(students)
print(students["student1"]["name"])
print(students["student2"]["course"])
print(students["student1"]["age"])