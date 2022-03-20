def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


a = int(input("Digite o valor de a: ").strip())
b = int(input("Digite o valor de b: ").strip())
c = int(input("Digite o valor de c: ").strip())

print("A área do triângulo é: ", heron(a, b, c))

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
    print("A área do triângulo é: ", heron(*t))
