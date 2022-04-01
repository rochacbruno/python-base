# Definição da classe
class Person:
    """Represents a Person"""

    # Atributos da classe
    name = "Jim Halpert"
    role = "Salesman"
    balance = 100

    # Métodos ou funções associadas
    def add_points(self, value):
        if self.role == "manager":
            value *= 2
        self.balance += value


jim = Person()
jim.add_points(500)
print(jim.balance)


print(Person.__dict__)


pessoa1 = Person()
pessoa2 = Person()

print(pessoa1.name)
print(pessoa2.name)


print(id(pessoa1))
print(id(pessoa2))

print(id(pessoa1.name))
print(id(pessoa2.name))
print(id(Person.name))

pessoa1.add_points(100)
pessoa2.add_points(200)

print(pessoa1.__dict__)
print(pessoa2.__dict__)


class Fruit:
    name = "apple"


apple = Fruit()
apple.color = "red"

banana = Fruit()
banana.color = "yellow"

print(apple.name, apple.color)
print(banana.name, banana.color)


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color


apple = Fruit(name="Apple", color="red")
banana = Fruit("Banana", color="yellow")

print(apple.name, apple.color)
print(banana.name, banana.color)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        perimeter = self.a + self.b + self.c
        s = perimeter / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


triangle = Triangle(5, 12, 13)
print(triangle.area())

triangle.a = 10
print(triangle.area())
