import json

# Python dictionary
data = {
    "name": "Ilma",
    "age": 22,
    "city": "Aligarh",
    "skills": ["Python", "Java", "JavaScript"],
    "is_student": True
}

# Writing dictionary into JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading JSON file
with open("data.json", "r") as f:
    result = json.load(f)

print(result)
print(result["name"])
print(result["skills"])
