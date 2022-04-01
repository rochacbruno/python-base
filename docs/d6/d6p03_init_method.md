# Inicialização de objetos

**E como fazemos para criar objetos diferentes a partir de uma mesma classe?**

Para que objetos criados a partir de uma mesma classe tenham atributos distintos
estes atributos devem ser atribuidos diretamente na instância.

```py
jim = Person()
jim.name = "Jim Halpert"
```

Ou dentro de métodos, os métodos por padrão atuam em cada uma das instancias separadamente, veja o exemplo de nosso método
`add_points`

```py
def add_points(person, value):
    if person.role == "manager":
        value *= 2
    person.balance += value
```

Um método de **instância** sempre recebe como injeção de dependência em seu
primeiro parametro a própria instancia e quando queremos atribuir algum valor
a instância sem afetar outros objetos da mesma classe sempre devemos fazer isso
na instância, no nosso exemplo chamamos de `person` e, `def add_points(person,`
mas por convenção é comum nomearmos esse argumento como `**self**`.

```py
pessoa1.add_points(100)
pessoa2.add_points(200)
print(pessoa1.__dict__)
print(pessoa1.balance)
print(pessoa2.__dict__)
print(pessoa1.balance)
{'balance': 200}
200
{'balance': 300}
300
```

Vamos utilizar um exemplo mais simples para ficar mais fácil de compreender
a estrutura de uma classe.

Digamos que em nosso programa desejamos representar frutas.

```py
class Fruit:
    name = "apple"


apple = Fruit()
apple.color = "red"

banana = Fruit()
banana.color = "yellow"

print(apple.name, apple.color)
print(banana.name, banana.color)
```
```
apple red
apple yellow
```

**Algo está errado! a nossa segunda fruta deveria ter no name=banana**

Lembre-se, neste caso devemos ou efetuar a alteração explicitamente em cima
do objeto `banana` como fizemos com a cor, ou então usar um método de inicialização.

O protocolo de classes do Python especifica que sempre que existir um método
chamado `__init__` em uma classe, esse método será chamado assim que o objeto for criado
para inicializar a instância do objeto, e esse método é bastante útil para inicializar
objetos com atributos distintos.


```py
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color


apple = Fruit(name="Apple", color="red")
banana = Fruit("Banana", color="yellow")

print(apple.name, apple.color)
print(banana.name, banana.color)
```
```
Apple red
Banana yellow
```

Desta forma nós temos uma classe `Fruit` que em sua definição tem apenas um 
método chamado `__init__` que por sua vez inicializa instancias cada uma com
seu conjunto separado de atributos e valores.

**Se uma classe é uma estrutura similar a um dicionário e em um dicionário nós
também podemos armazenar valores e funções qual o motivo de usarmos classes?**

Vamos analisar isso em mais um exemplo prático, lembra da nossa função que 
calcula a area de um triangulo?

```py
def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
```

e o uso que fizemos dessa função

```py
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
```

Isso foi feito no modelo imperativo onde a função `heron` ficou separada dos dados
`(a, b, c)` presente em cada triangulo, vamos reescrever usando P.O.O.

```py
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
```
```
30.0
```

Qual a vantagem? é que agora podemos alterar o triangulo interativamente e
recalcular sua área usando o método que está associado.

```py
triangle.a = 10
print(triangle.area())
```
```
56.99506557588999
```

O principal motivo para definirmos os nossos próprios tipos de dados é a padronização,
e os outros estão explicados nos 4 pilares da O.O que veremos a seguir.