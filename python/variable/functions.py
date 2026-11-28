def student_subjects():
    subjects = ["Python", "Java", "Maths", "English"]
    for subject in subjects:
        print(subject)
    print("First Subject:", subjects[0])
    print("Last Two Subjects:", subjects[-2:])
    print("Total Subjects:", len(subjects))
    subjects.reverse()
    print("Reversed Subjects:", subjects)
student_subjects()



items = {"bag": 500,"shoes": 1200,"crop_top": 800}
def calculate_total():
    total = 0
    for price in items.values():
        total += price
    return total
bill = calculate_total()
print("Total Shopping Bill:", bill)