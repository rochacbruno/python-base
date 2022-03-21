people = [
    {"name": "Jim Halpert", "balance": 500, "role": "Salesman"},
    {"name": "Dwight Schrute", "balance": 100, "role": "Manager"},
]


def add_points(person, value):
    if person["role"] == "manager":
        value *= 2
    person["balance"] += value
    return person


for person in people:
    add_points(person, 100)

print(people)
