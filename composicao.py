"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]


# estilo funcional
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()

# estilo imperativo
print("Estilo procedural")


def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == "b"


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
