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