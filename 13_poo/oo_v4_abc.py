class Fruit:  # Classe abstrata
    kingdom = "vegetalia"


class Apple(Fruit):  # Classe Material
    colors = ["red", "white"]
    image = "🍎"


fruit1 = Apple()  # OK instancia criada a partir da classe material
print(fruit1.kingdom)

fruit2 = Fruit()  # NÃO ok, instancia criada a partir da classe abstrata
print(fruit2.kingdom)

from abc import ABC


class Fruit(ABC):  # por convenção uma classe abstrata
    kingdom = "vegetalia"
