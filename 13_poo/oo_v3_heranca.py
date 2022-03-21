class Fruit:  # Classe abstrata
    kingdom = "vegetalia"


class Apple(Fruit):  # Classe Material
    colors = ["red", "white"]
    image = "🍎"


class Watermelon(Fruit):
    colors = ["green", "red"]
    image = "🍉"


class Pineapple(Fruit):
    colors = ["yellow", "green"]
    image = "🍍"


for fruit in [Apple(), Watermelon(), Pineapple()]:
    print(fruit.image, fruit.kingdom, fruit.colors)
