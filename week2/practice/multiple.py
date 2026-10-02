students = [
    {"name": "Hermione", "house": "gryffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "gryffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "gryffindor", "patronous": "Some long weird name"},
    {"name": "Draco", "house": "slytherin", "patronous": None}
]

for student in students:
    for quality in student:
        print(f"{quality} is {student[quality]}")
    print("-------------------------")