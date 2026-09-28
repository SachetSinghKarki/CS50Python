# students=["Luna", "Leo", "Adam"]
# country=["Deutschland", "France","Austria"]

# I feel its like objects in javascript

students = {
    "Luna":"DeutschLand",
    "Leo":"Austria",
    "Adam":"France",
    "Alie":"United Kingdom"
}

# print(students["Luna"])
# print(students["Leo"])
# print(students["Adam"])
# print(students["Alie"])

for student in students:
    print(student, students[student], sep=" -> ")