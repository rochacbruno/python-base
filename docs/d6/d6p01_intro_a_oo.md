# Programação Orientada a Objetos

## Objetos

Em Python tudo é objeto, desde o começo deste treinamento já estamos utilizando
Objetos e já vimos aqui também que um objeto é formado sempre por um `valor`, um
`tipo` e um `id` de memória.

Até agora criamos nossos programas, como por exemplo o projeto `dundie`
utilizando apenas os tipos de dados primários e compostos embutidos no Python
como `int`, `str`, `list` e `dict` a além disso usamos `funções` para organizar
e tornar o código menos repetitivo.

## Paradigmas

Paradigma de programação é o modelo utilizado para expressar a lógica e manter
o estado dos valores de um programa, existem alguns paradigmas sendo os mais 
famosos: Procedural, Declarativo, Funcional e Orientação a Objetos.

Apesar de usarmos muitos objetos e biliotecas que aplicam a orientação a objetos
como fizemos com `smtplib.SMTP`, `rich.Table` e `log.Logger` nós ainda não 
tivemos que criar nossos próprios objetos e você percebeu que é perfeitamente
possível criar um programa em Python completo sem a necessidade de saber sobre
orientação a objetos.

Existem linguagens que são mais restritas como por exemplo algumas que são 
puramente funcionais como Haskell e Scheme, e outras como Java e C# que são
estritamente orientadas a objetos.

Em Python conseguimos usar uma mistura dos paradigmas imperativo, funcional e 
orientado a objetos, podemos orientar todo o nosso programa a apenas um deles ou
na maioria dos casos juntar esses paradigmas em uma única solução.

Vamos analisar alguns paradigmas que podemos aplicar com Python:


### Paradigma Imperativo (ou procedural)

Em nosso projeto, nós aplicamos programação procedural e utilizamos um dicionário 
compartilhado para armazenar o estado do programa e as suas informações.

```py
people = [
    {
        "name": "Jim Halpert",
        "balance": 500,
        "role": "Salesman"
    },
    {
        "name": "Dwight Schrute",
        "balance": 100,
        "role": "Manager"
    }
]

def add_points(person, value):
    if person["role"] == "manager":
        value *= 2
    person["balance"] += value
    return person

for person in people:
    add_points(person, 100)

print(people)
```

Ao executar a saida será:

```py
[{'name': 'Jim Halpert', 'balance': 600, 'role': 'Salesman'}, 
{'name': 'Dwight Schrute', 'balance': 200, 'role': 'Manager'}]
```
Repare que o `balance` dos funcinários foi aumentado.

No exemplo acima temos um objeto do tipo `list` que em cada uma de suas posições
tem um objeto do tipo `dict` que contém chaves `str` e valores `str` e `int`.

Nós também criamos uma `função` chamada `add_points` que recebe um dict `pessoa`
e um valor `value` e então aplica uma regra de negócio.

Na programação procedural utilizamos estruturas de dados como um `dict` para
manter os dados e objetos desacoplados como `function` para definir comportamento.

### Misturando com funcional

Poderiamos neste mesmo programa utilizar um pouco de programação funcional ao
substituir nosso `for` por uma abordagem funcional.

```py
map(lambda person: add_points(person, 100), people)
```

E ao executar a saída será:

```py
[{'name': 'Jim Halpert', 'balance': 500, 'role': 'Salesman'}, 
{'name': 'Dwight Schrute', 'balance': 100, 'role': 'Manager'}]
```

Repare que nada aconteceu com os dados, apesar de termos declarado o `map`
ele não foi executado e não teve `side effects` **ainda** em nossos dados.

Construções como `map` e `filter` e `reduce` tem avaliação preguiçosa, nós podemos
declarar esses objetos mas a execução acontecerá somente quando consumirmos.

```py
result = map(lambda person: add_points(person, 100), people)
print(list(result))
```

Pensando em paradigma funcional daria para escrevermos este mesmo código de
forma que ele não faria alterações nos dados inicias mas sim criaria uma nova
coleção de dados sem `side effects` e para atingir isso deveriamos escrever
funções "puras" que retornam sempre novos dados sem modificar dados existentes.

```py

def add_points(person, value):
    data = person.copy()  # copiamos o valor de entrada ao invés de altera-lo
    if data["role"] == "manager":
        value *= 2
    data["balance"] += value
    return data


result = map(lambda person: add_points(person, 100), people)
print("Resultado funcional:", list(result))
print("Dados originais sem side effects:", people)
```

### Orientação a objetos

A programação orientada a objetos surgiu em 1970 e naquela época os programas
eram escritos das maneiras procedural e funcional, Alan Kay, um matemático
que foi trabalhar na Xerox desenvolvendo uma espécie de tablet chamado Dynabook
sentiu a necessidade de criar uma linguagem de programação onde fosse possível
representar as estruturas de dados de uma maneira mais próxima a objetos do
mundo real e criou a linguagem `Smalltalk` a primeira linguagem orientada a 
objetos e que acabou por influenciar a maioria das linguagens que usamos hoje
em dia.

A orientação a objetos é construida utilizando alguns componentes como

- Classes: Usando a keyword `class` definimos um tipo de objeto.
- Objetos: Instancias criadar a partir das classes.
- Atributos: As classes podem definir valores nomeados assim como os dicionários.
- Métodos:  As classes podem definir funções associadas.

Exemplo:

```py
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

jim = Person()  # Instanciação de um objeto a partir da classe

jim.add_points(500)  # Chamada de método associado

print(jim.balance)  # Acesso a atributo
```

Usamos a palavra `class` seguida de um nome para atribuir esse nome ao objeto
de memória que irá conter o código e o escopo de dados da classe.

A regra de estilo agora difere das funções e precisa ter suas palavras iniciadas
 em Maiusculo portanto uma classe para representar uma maçã vermelha se chamaria
 `RedApple` ao invés de `red_apple` ou `Red_Apple`, este padrão é chamado de 
 `PascalCase` ou `UpperCamelCase`.

A classe é um namespace, portanto dentro da sua definição iniciamos um novo 
bloco de código após os `:` que seguem o seu nome e a partir dai todas as 
regras que já conhecememos continuam valendo, podemos dentro do corpo da classe
definir variáveis usando qualquer tipo de dados mas agora chamaremos essas
variáveis de `atributos` e também podemos escrever funções dentro da classe
e essas funções serão associadas a esta classe e chamaremos de `métodos`.

Uma classe é uma estrutura de dados composta e de fato internamente o Python
usará um dicionário para armazenar suas informações:

```py
print(Person.__dict__)
```
```py
{
'name': 'Jim Halpert', 
'role': 'Salesman', 
'balance': 100, 
'add_points': <function Person.add_points at 0x7fa45a441fc0>, 
'__doc__': 'Represents a Person'
}
```

Esses atributos que consultamos em `Person.__dict__` são chamados `atributos de classe`
e eles serão atribuidos a todos os objetos criados a partir desta mesma classe.

```py
pessoa1 = Person()
pessoa2 = Person()

print(pessoa1.name)
print(pessoa1.__dict__)
print(pessoa2.name)
```
```py
Jim Halpert
Jim Halpert
```

Repare que as nossas 2 instancias `pessoa1` e `pessoa2` agora possuem o mesmo
valor no atributo `nome` e faria mais sentido principalmente para nosso projeto
`dundie` termos pessoas com nomes diferentes mas todos os objetos criados
a partir de uma mesma classe possuem todos os atributos definidos no corpo da
classe.

Quando fazermos o instanciamento de um objeto usando uma classe, o Python cria
um novo objeto na memória para cada instância.

```py
print(id(pessoa1))
print(id(pessoa2))
140015571746576
140015571746528
```

porém os atributos do corpo da classe
sempre serão os mesmos.

```py
print(id(pessoa1.name))
print(id(pessoa2.name))
140197426339504
140197426339504
```

Lembre-se que a atribuição de `name` ocorreu no corpo da classe, portanto 
ocorreu uma única vez quando a classe foi criada.

```py
print(id(Person.name))
140197426339504
```

**E como fazemos para criar objetos diferentes a partir de uma mesma classe?**

Para que objetos criados a partir de uma mesma classe tenham atributos distintos
estes atributos devem ser definidos dentro de métodos, os métodos por padrão
atuam em cada uma das instancias separadamente, veja o exemplo de nosso método
`add_points`

```py
def add_points(self, value):
    if self.role == "manager":
        value *= 2
    self.balance += value
```

Um método de **instância** sempre recebe como injeção de dependência uma parametro
que por convenção é chamado de **self** e quando queremos atribuir algum valor
a instância sem afetar outros objetos da mesma classe sempre devemos fazer isso
na instância **self** como fizemos no `add_points` dessa maneira:

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

**Algo está errado! a nossa segunda frura deveria ter no name=banana**

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


## Os Pilares da Orientação a Objetos

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

##### Propriedades

A outras maneira de encapsular no Python é usando propriedades, é uma forma
bastante elegante e que utiliza um protocolo chamado `Descriptor`,
este modelo se parece bastante com o que vemos em outras linguagens de programação
como Java utilizando getters, setters e deleters.

```py
class Conta:
    _tipo_de_conta = "corrente"
    __id_interno = 985645

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    @property  # getter
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @saldo.deleter
    def saldo(self):
        self._saldo = 0


conta = Conta(cliente="Bruno")
conta.saldo = 100
conta.saldo = -10
print(conta.saldo)
```
```
90
```

```py
del conta.saldo
print(conta.saldo)
```
```
0
```

Uma grande vantagem em usar o padrão de properties é a possibilidade de
definir métodos internamente e expor como atributos sem a necessidade de 
parenteses para chamada.


## Python data Model e Protocolos

Tudo o que falamos até agora foi baseado na teoria padrão de O.O aplicada a Python
mas o fato é que a teoria de orientação a objetos que geralmente é aplicada a
linguagens como Java e C# não se aplica a Python da mesma maneira e isso acontece
pois Python é uma linguagem mais orientada a protocolos do que a classes.

Isso é visivel na maior parte das construções da própria linguagem, por exemplo
podemos imprimir listas e dicionários no stdout mesmo eles não sendo strings.

```py
dados = [1, {"key": "value¨"}, True]
print(dados)
```
```
[1, {'key': 'value¨'}, True]
```

E isto só é possivel por causa do protocolo `Printable` que faz com que todos
os objetos que implementem `__str__` possam ser impressos no terminal.

### Printable

Vamos fazer em um objeto customizado:

```py
class Cor:
    icon = "⬜"

class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())
```
```
<__main__.Amarelo object at 0x7f677c9a3fd0>
<__main__.Azul object at 0x7f677c9a3fd0>
<__main__.Vermelho object at 0x7f677c9a3fd0>
```

Por padrão o python irá imprimir o `__repr__` que é a representação dos objetos,
mas podemos customizar implementando `__str__`


```py
class Cor:
    def __str__(self):
        return self.icon

...
print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())
```

```
🟨
🟦
🟥
```

### Addible

Todo objeto que implementa o protocolo Addible pode ser somado um a outro.

```py
"Bruno" + "Rocha"
6 + 7
42.1 + 47.9
True + True
```
E podemos definir nossos próprios objetos que respondem a este mesmo protocolo.

```py
class Cor:
    def __str__(self):
        return self.icon

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()

class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


print("Cores secundárias")
print(Amarelo() + Vermelho())
print(Azul() + Amarelo())
print(Vermelho() + Azul())
```
```
🟧
🟩
🟪
```

### Iterable

Os objetos que implementam `__iter__` podem ser iterados por exemplo em um loop
`for`:

```py
nome = "Bruno"
for letra in nome:
    print(letra)
```
```
B
r
u
n
o
```

E customizando em nossos objetos pata torna-los Iterable:

```py
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])


print("rgb")
rgb = Paleta(Vermelho(), Verde(), Azul())
for cor in rgb:
    print(cor, end="")
```
```
rgb
🟥🟩🟦
```

### Container

Containeres são objetos em que podemos consultar com o lookup `in`

```py
numeros = [1, 2, 3]
print(3 in numeros)
```
```
True
```

E para transformar nossos objetos em Container podemos implementar `__contains__`:


```py
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]


print("red in rgb?")
rgb = Paleta(Vermelho(), Verde(), Azul())
print("🟥" in rgb)
```
```
True
```

### Sized

Todo objeto que possui um tamanho e que expoe este tamanho através da função
`len` é um objeto `Sized`.

```py
nome = "Bruno"
print(len(nome))
```
```
5
```

Logo

```py
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)


print("rgb size")
rgb = Paleta(Vermelho(), Verde(), Azul())
print(len(rgb))
```
```
3
``` 

### Collection

Protocolos não precisam ser usados sozinhos, existem objetos que implementam
mais de um protocolo como por exemplo as listas e dicionários.

```py
numeros = [1, 2, 3]
len(numeros)  # sized
3 in numeros  # container
for numero in numeros:  # Iterable
    print(numero)
```

Os objetos que implementam Sized + Container + Iterable são chamados de `Collection`


```py
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])
```

Uma `Paleta` é uma `Collection` de `Cor`es.


### Subscriptable

```py
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._cores[item]
        elif isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor

rgb = Paleta(Vermelho(), Verde(), Azul())
print(rgb[0])
print(rgb["azul"])
```
```
🟥
🟦
```

Mais protocolos estão listados em https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes


## Protocolos default e Data Model

Quando criamos um objeto e não implementamos nenhum protocolo o Python assim
mesmo utiliza alguns protocolos padrão e são eles:

```py
class Thing:
    ...

thing = Thing()
print(thing)  # __repr__ Representable
thing == 1  # __eq__ Equality Comparable
```

E toda classe herda da classe base `object` que contém implementações padrão
para os métodos:

```py
__new__              # Construtor chamado antes de criar a intância
__init__             # Inicializador chamado após a instância é criada
__init_subclass__    # Inicializador de subclasses
__repr__             # Imprime a representação em string
__str__              # chama __repr__ por padrão
__setattr__          # executado sempre que atribuimos com obj.name = value
__getattr__          # executado quando acessamos obj.name
__delattr__          # executado quando apagamos com `del obj.name`
__getattribute__     # executado quando um atributo não é encontrado
__dir__              # lista todos os atributos e métodos
```


