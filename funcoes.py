"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""


# Solid - Single Responsibility


def f(x):  # assinatura
    result = 5 * (x / 2)
    ...
    return result


def double(x):
    return x * 2


valor = double(f(10))

print(valor)
print(valor == 50)


def print_in_upper(text):
    """Procedure with no explicit return"""
    print(text.upper())
    # implicit return None


print_in_upper("bruno")

####


def heron(a, b, c):
    """Calcula a area de um triangulo"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area**0.5  # math.sqrt(area)


triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]

for t in triangulos:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")


####


def nome_da_funcao():
    print("Hello funcao")
    return 1


result = nome_da_funcao()
print(result)
