people = [
    {"name": "Jim Halpert", "balance": 500, "role": "Salesman"},
    {"name": "Dwight Schrute", "balance": 100, "role": "Manager"},
]


def add_points(person, value):
    data = person.copy()
    if data["role"] == "manager":
        value *= 2
    data["balance"] += value
    return data


result = map(lambda person: add_points(person, 100), people)
print("Resultado funcional:", list(result))

print("Dados originais sem side effects:", people)
