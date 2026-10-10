students = [
    {"name":"Leo", "house":"London"},
    {"name":"Luna", "house":"Berlin"},
    {"name":"Loca", "house":"Paris"},
    {"name":"Lizza", "house":"Los Angeles"},
    {"name":"Loofa", "house":"Manchester"},
]

# houses =[]

# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)

houses = set()
for student in students:
    houses.add(student["house"])
    
for house in sorted(houses):
    print(house)