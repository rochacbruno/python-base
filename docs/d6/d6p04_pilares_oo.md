# Os Pilares da Orientação a Objetos

Muitos teóricos estudaram a linguagem de Alan Kay e determinaram alguns padrões
de projeto e entre eles o que se destaca são os 4 pilares da P.O.O que são

#### Abstração

A Capacidade de representar um objeto abstrato do mundo real ou do dominio do 
programa sendo desenvolvido.

```py
class Person:
    """Represents a Person"""
    kingdom = "animalia"

class Fruit:
    """Represents a fruit"""
    kingdom = "vegetalia"

class Animal:
    """Represents an animal"""
    kingdom = "animalia"
```

E então a partir desta classe abstrata criar novas classes derivadas que veremos
em detalhes no pŕoximo item `herança`.

#### Herança

A capacidade de uma classe herdar atributos e comportamento a partir de outra
classe.

```py
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
```

Em teoria, deveriamos ser incapazes de criar objetos a partir das classes
abstratas e apenas conseguir a partir de classes materiais em nosso exemplo 
deveriamos ser impedidos de criar uma instancia de um objeto diretamente a 
partir da classe abstrata `Fruit` mas em Python todas as classes são abertas e 
nada nos impede de fazer:

```
fruit1 = Apple()  # OK instancia criada a partir da classe material
print(fruit1.kingdom)

fruit2 = Fruit()  # NÃO ok, instancia criada a partir da classe abstrata
print(fruit2.kingdom)
```

> No mundo real, não existe um objeto chamado `Fruta` sempre temos uma derivação
> de fruta com um nome material e caracteristicas bem definidas como "Maçã", 
"Banana" etc..

A linguagem Python segue a filosofia de "Somos todos adultos e sabemos o que
fazemos", portanto este tipo de **regra** é aplicada mais a título de convenção
e sempre que uma classe é abstrata nós podemos deixar isso explicito usando uma
Abstract Base Class

```py
from abc import ABC
class Fruit(ABC):
    kingdom = "vegetalia"
```

Ainda não somos impedidos de criar a instância mas agora está explicito que não
deveriamos fazer.

#### Polimorfismo

Polimorfismo em Python está ligado aos **protocolos** e isso nós já vimos aqui
no treinamento várias vezes quando usamos abstrações como `in` para invocar o
procolo `__contains__` tanto em listas, tuplas, sets e dicionários, 4 objetos
diferentes mas que podem ser usados em um mesmo contexto.

```py
"valor" in objeto  # objeto pode ser qualquer tipo que implementa `__contains__` 
```

Um exemplo prático com uma classe customizada:

```py
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
```
```
woof woof
meow meow
pew pew
```

A função `print_sound` é polimórfica, ela estabelece que o objeto recebido
desde que ele exponha um método chamado `make_sound` ela não se importa com
o tipo especifico deste objeto.

Esta é uma caracteristica de linguagens de programação dinâmicas conhecida
como **Duck Typing** ou **Tipagem Pato**.

> Se anda como um pato, faz barulho como um pato e se parece com um pato, então
> é um pato! não importa se é um cachorro que aprendeu a fazer "quack".

#### Encapsulamento

Encapsulamento é a capacidade de um objeto esconder sua implementação interna
e expor apenas o que for conveniente, em Python isso pode ser feito de algumas
maneiras:

##### Convenções de nomes:

```py
class Conta:
    _tipo_de_conta = "corrente"
    __id_interno = 985645

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    def depositar(self, value):
        self._saldo += value

    def sacar(self, value):
        self._saldo -= value
        return value

    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo

```
```py
conta = Conta(cliente="Bruno")
print(dir(conta))
```
```py
# Privado via name mangling
# Não é possível acessar `conta.__id_interno` mas por conta e risco:
'_Conta__id_interno',  

# Protegido por convenção de nome:
# É possível acessar `conta._saldo` mas o `_` denota que esse valor
# deve ser acessado apenas internamente dentro dos métodos da própria classe.
'_saldo', 
'_tipo_de_conta', 

# Atributos e métodos públicos
'cliente', 
'consultar', 
'depositar', 
'sacar'
```

O encapsulamento em Python segue novamente aquela filosofia dos `consent adults`, ou
**somos todos adultos e responsáveis pelos nossos atos**, ou seja, tá avisado ali
na convenção de nomes que não devemos acessar o `__id_interno` se acessarmos pode 
dar algum problema.

Geralmente quando uma classe é escrita definindo atributos e métodos protegidos
isso significa que a funcionalidade encapsulada está disponível e abstraida em 
métodos públicos, não precisamos alterar o `_saldo` diretamente, mas podemos chamar
o método `depositar`

```py
conta = Conta(cliente="Bruno")
conta.depositar(100)
conta.sacar(10)
print(conta.consultar())
print(conta.cliente)
```
```
90
Bruno
```

A segunda maneira é utilizando **propriedades** que nós abordaremos na próxima aula.