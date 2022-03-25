# Python moderno

Chamamos de **Python Moderno** O Python com suporte a anotação de tipos, a partir
do Python 3.5 Python incorporou um módulo chamado `typing` e passou a permitir
a **anotação** dos tipos em atribuições como criação de variáveis, funções e classes.


Antes das type annotations:

```py
from decimal import Decimal

produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5


def calcula_total(valor, quantidade):
    return valor * quantidade


total_da_compra = calcula_total(valor, quantidade)


print(f"A compra de {quantidade} {produto}s deu R$ {total_da_compra}")
```

Como tratamos de valor monetário queremos garantir que o total_da_compra
seja do tipo `Decimal`

```py
...
total_da_compra = calcula_total(valor, quantidade)

print(type(total_da_compra))  # vamos ver o tipo de total_da_compra

print(f"A compra de {quantidade} {produto}s deu R$ {total_da_compra}")

```

```bash
<class 'decimal.Decimal'>
A compra de 5 Canetas deu R$ 22.5
```

Até aqui parece tudo bem mas podemos livremente alterar os tipos das variáveis definidas em Python já que Python é uma linguagem dinâmica e que permite variable shadowing.


```py
...
valor = 5.3
total_da_compra = calcula_total(valor, quantidade)

print(type(total_da_compra))

print(f"A compra de {quantidade} {produto}s deu R$ {total_da_compra}")

```
```bash
<class 'float'>
A compra de 5 Canetas deu R$ 26.5
```

Repare que o fato de reatribuirmos o valor para `5.3` fez com que ele se tornasse
`float` e isso é indesejado pelo nosso programa.

Precisamos de algum nível de garantia de tipos e ai que entram as type annotations.

## Type Annotations

Como o nome diz **anotações** são apenas marcas que colocamos em nosso código,
este conceito é também chamado de **type hints** (dicas de tipo) e o interpretador
Python por enquanto não vai fazer nada com as anotações que fizermos, porém
podemos utilizar ferramentas externas para nos ajudar a não cometer esse erro.


Para adicionar uma anotação usamos a sintaxe `nome: T` em qualquer atribuição
sendo que `T` pode ser qualquer tipo definido no módulo `typing`, classes criadas
por nós ou a apartir do Python 3.8 também pode ser qualquer tipo literal do Python 
como `nome: str`, `numero: int`, `flag: bool`, ou seja, junto com o nome de uma
variável também colocamos qual o seu tipo.

E além de poder fazer isso nas atribuições nós também podemos fazer nos retornos de função:

> NOTA: lembre-se que paramêtros de uma função são atribuições.

Portanto em nosso código podemos fazer isso na função `calcula_total`


```py
def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade
```

> **ATENÇÃO** ao executar NADA terá mudado e continuamos recebendo um `float`

```bash
<class 'float'>
A compra de 5 Canetas deu R$ 26.5
```

Então pera ai, se Python vai ignorar minha anotação `-> Decimal` e continuar
me retornando `float` para que serve a anotação?

## Mypy

Existem algumas ferramentas de análise estática (lembra dos linters?) que são
capazes de vasculhar o código e apontar discrepancias de tipos, uma dessas 
ferramentas é criada e mantida pelo próprio criador do Python, o Guido Van Rossum.

Mas é uma ferramenta externa que precisa ser isntalada.

```bash
pip install mypy
```

E agora podemos executar a verificação com 

```bash
mypy arquivo.py
arquivo.py:12: error: Incompatible types in assignment (expression has type "float", variable has type "Decimal")
Found 1 error in 1 file (checked 1 source file)
```

Portanto essa ferramenta passa a fazer parte dos **linters** do nosso projeto e 
podemos inclusive rodar no CI do Github para garantir que nenhum código será
inserido com discrepância de tipos.

Não precisamos sair anotando tudo em nosso código, a anotação de tipos em Python é
gradual, repare que o Mypy reclamou somente desta variável e inclusive podemos
configurar o mypy para o nível de restrição que desejarmos.

Com as mensagens de erro do Mypy podemos ir ajustando o código para ter
garantia de tipos.

```py
valor = Decimal(5.3)
```

Nós até poderiamos fazer a anotação tipos em toda as atribuições do programa como:

```py
from decimal import Decimal
produto: str = "Caneta"
valor: Decimal = Decimal(4.5)
quantidade: int = 5


def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade


valor = Decimal(5.3)  # anotação de tipo já efetuada na linha 3
total_da_compra: Decimal = calcula_total(valor, quantidade)
```

Mas a parte mais interessante de Python é o fato da linguagem ser dinâmica,
e a melhor coisa da tipagem no Python é o fato dela ser opcional e gradual.

Portanto a recomendação é anotar apenas assinaturas de funções e métodos e não
as atribuições diretas de um programa.

```py
from decimal import Decimal

produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5


def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade


valor = Decimal(5.3)
total_da_compra = calcula_total(valor, quantidade)

print(type(total_da_compra))

print(f"A compra de {quantidade} {produto}s deu R$ {total_da_compra}")
```
```bash
Success: no issues found in 1 source file
```

Até porque o Mypy é esperto o suficiente para automaticamente **pegar** erros
em reatribuições:


```py
...

produto = 1  # era string e mudamos para inteiro
valor = Decimal(5.3)
total_da_compra = calcula_total(valor, quantidade)
...
```
```
arquivo.py:12: error: Incompatible types in assignment (expression has type "int", variable has type "str")
Found 1 error in 1 file (checked 1 source file)
```

## Composição de tipos

Podemos anotar paramêtros que recebem tipos variados e para isso podemos usar
um tipo especial chamado `Union`

Exemplo:

Se chamamos 

```py
calcula_total(Decimal(1), 4)  # Ok

# e

calcula_total(1, 4)  # erro

```
```bash
error: Argument 1 to "calcula_total" has incompatible type "int"; expected "Decimal"
```

Mas e se de fato quisermos que a função também aceita inteiros?


```py
from typing import Union
...
def calcula_total(valor: Union[Decimal, int], quantidade: int) -> Decimal:
    return Decimal(valor * quantidade)


calcula_total(1, 4)
```
```bash
Success: no issues found in 1 source file
```

Para usar esses tipos pré definidos precisamos importar da biblioteca `typing`
https://docs.python.org/3/library/typing.html

E nela existem outras definições interessantes.


> **Nota**: No Python 3.10 tem uma novidade, agora não precisamos mais 
> importar o tipo `Union` basta usarmos o operador `|` portanto
> ao invés de `Union[Decimal, int]` usamos `Decimal | int`

```py
def calcula_total(valor: Decimal | int, quantidade: int) -> Decimal:
    return Decimal(valor * quantidade)
```

Outros tipos especiais interessantes são:

- `Optional[T]` - para quando um argumento pode ser `None` ou `T`
- `NoReturn` para declarar que a função não tem retorno explicito
- `Any` para determinar que o argumento aceita qualquer tipo.

E alguns que implementam tipos especificos mas que a partir do Python 3.9 
podem ser substituidos pelos tipos literais.

- `Dict` para determinar um dicionário
- `List` para uma lista
- `Set` para um set
- `Tuple` para uma tupla

E é possivel compor as anotações vamos a alguns exemplos:


Uma função que espera um dicionário onde a chave é `str` e o valor é `float`

```py
# antes do Python 3.9
def function(arg: Dict[str, float]):
    ...

# após o Python 3.9
def function(arg: dict[str, float]):
    ...
```

Uma função que espera uma lista de inteiros

```py
# antes do Python 3.9
def function(arg: List[int] | Tuple[int]):
    ...

# após o Python 3.9
def function(arg: list[int] | tuple[int]):
    ...
```

Uma função que espera um set contendo inteiros porém opcional

```py
# Antes do Python 3.9
def function(arg: Optional[Set[int]]):
    ...

# após o Python 3.9
def function(arg: set[int] | None):
    ...


function(set([1, 2]))
function(None)
```

## Type alias

Para deixar a escrita mais legivel também podemos criar type alias,
que são tipos próprios definidos a partir de uma composição de tipos.

Digamos que tenhamos um dicionário indexado por `str` onde em cada chave temos
um sub dicionário também indexado por `str` e que os seus valores podem ser
qualquer tipo.

Anotação

`dict[str, dict[str, Any]]` 

que representa o seguinte valor:

```py
{   
    "joe@doe.com": {  
        "name": "Joe",
        "points": 10
    }
}
``` 

Ao invés de anotarmos uma função com:


```py
def funcao(dados: dict[str, dict[str, Any]]):
    ...
```

Podemos criar um alias para nosso tipo:


```py
DictPessoa = dict[str, dict[str, Any]]


def funcao(dados: DictPessoa):
    ...

```


Mas é claro que neste examplo pode valer mais a penas deixar de trabalhar com 
dicionários e transformar seus dados em uma classe.


```py
class Pessoa:
    def __init__(self, pk: str, name: str, points: int):
        self.pk = pk
        self.name = name
        self.points = points


def funcao(dados: Pessoa):  # usamos a própria classe para anotar
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

funcao(dados)

```

E para deixar isso ainda mais fácil, Python adicionou no 3.7 as `dataclasses`
que entre outras coisas, substitui a necessidade do nosso `__init__`

https://docs.python.org/3/library/dataclasses.html?highlight=dataclass#module-dataclasses

```py
@dataclass
class Pessoa:
    pk: str
    name: str
    points: int


def funcao(dados: Pessoa):
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

funcao(dados)
```

