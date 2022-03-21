objetos = [
    ["Bruno"],  # list
    ("Bruno",),  # tuple
    set(["Bruno"]),  # set
    {"Bruno": 1},  # dict
]

for objeto in objetos:
    print("Bruno" in objeto)  # todos implementam __contains__


class Dog:
    def make_sound(self):
        return "woof woof"


class Cat:
    def make_sound(self):
        return "meow meow"


class Bird:
    def make_sound(self):
        return "pew pew"


def print_sound(obj):
    print(obj.make_sound())


print_sound(Dog())
print_sound(Cat())
print_sound(Bird())

# Todos implementam `make_sound`
