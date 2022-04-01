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
    def add_points(person, value):
        if person.role == "manager":
            value *= 2
        person.balance += value

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
