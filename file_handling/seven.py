import json

# Initial data
students = [
    {"name": "Aman", "marks": 85},
    {"name": "Sara", "marks": 92}
]

# Writing initial data
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

# Reading existing data
with open("students.json", "r") as f:
    data = json.load(f)

# Adding a new student
new_student = {"name": "Rahul", "marks": 78}
data.append(new_student)

# Updating Sara's marks
for student in data:
    if student["name"] == "Sara":
        student["marks"] = 95

# Saving updated data
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)

# Displaying final data
with open("students.json", "r") as f:
    result = json.load(f)

print(result)
