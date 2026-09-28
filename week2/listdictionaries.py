customers = [
    {"name": "Leo", "house": "Berlin", "purchased": "Sausage"},
    {"name": "Luna", "house": "Munich", "purchased": "Apple"},
    {"name": "Adam", "house": "Hamburg", "purchased": "Juice"},
    {"name": "Alie", "house": "Frankfurt", "purchased": None},
]

for customer in customers:
    print(customer["name"], customer["house"], customer["purchased"] ,sep=" -> ")