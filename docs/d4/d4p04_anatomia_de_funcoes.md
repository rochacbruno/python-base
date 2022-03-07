# Qual o motivo de usarmos funções?

O primeiro motivo nós já vimos, que é a aplicação de funções matemáticas de acordo com suas respectivas fórmulas.

Mas as funções também podem ser usadas para simplesmente organizar o código provendo:

- Encapsulamento de código em escopo `protegido`
- Reutilização de código
- Composição com outras funções
- Compartilhamento em forma de bibliotecas de funções
- Organização de códigos semanticamente.

### Organização

```py
print("Welcome to the test.)
input("When you are ready press enter.)

name = input("name:")
print(f"It is nice to meet you {name}")

color = input("Quat is your favorite color?")
print(f"{color} is a great color!")

input("Describe yourself")
print("admirable!")

print("Goodbye.)
```

Organizando:

```py
def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.")


def ask_questions():
    name = input("name:")
    print(f"It is nice to meet you {name}")

    color = input("Quat is your favorite color?")
    print(f"{color} is a great color!")

    input("Describe yourself")
    print("admirable!")


def goodbye():
    print("Goodbye.)


welcome()
ask_questions()
goodbye()
```

Neste caso temos **procedimentos** armazenados como funções.

## Composição:

```py
names = ["Bruno", "Joao", "Bernardo", "Barbara", "Brian"]

def start_with_b(name):
    return name[0].lower() == "b"

names_with_b = list(filter(start_with_b, names))
```

## Anatomia das funções

As funções são formadas por alguns elementos:

- definição (ou atribuição) - `def nome_da_funcao`
- assinatura - Tudo o que estiver entre parenteses - `(a, b ,c)` e antes de `:`
- código interno
- valor de retorno - Tudo o que tiver depois de `return`

```python
def nome_da_funcao(a, b, c):
    return a + b + c
```

## Argumentos

Ao passar os argumentos para as funções podemos passa-los posicionalmente ou nomeadamente.

Argumentos posicionais:

```python
nome_da_funcao(1, 2, 3)
```

Argumentos nominais:

```python
nome_da_funcao(a=1, b=2, c=3)
```

A grande diferença é que no caso dos posiciais devemos nos atentar a sempre passar o valor correto na posição correta, enquanto nos nominais não precisamos nos preocupar com a ordem.

```python
nome_da_funcao(b=2, a=1, c=3)
```

E também podemos passar argumentos nomeados e posicionais ao mesmo tempo.

```python
nome_da_funcao(1, b=2, c=3)
```

Neste caso a regra é que os argumentos posicionais sempre são declarados antes dos nomeados.

A partir do Python 3.4 podemos ainda anotar os tipos de dados dos argumentos de uma função:

```python
def nome_da_funcao(a: int, b: int, c: int) -> int:
    return a + b + c
```

O trecho `a: int` indica que o argumento `a` é do tipo inteiro,
isto é chamado `type hint` ou `dica de tipo` em português, o Python não usa essa informação, ela serve apenas para o programador ter uma melhor experiência ao utilizar as funções e para ferramentas externas fazerem verificações. (ainda falaremos mais sobre esse tópico em breve)

Todas essas caracteristicas de uma função são o que chamamos de **assinatura de função** (nome, argumentos, ordem, tipos, tipo de retorno)

Anteriormente já falamos um pouco sobre **tuplas** e sobre como podemos fazer coisas interessantes com elas como atribuição de multiplas variáveis e desempacotamento.

```python
coordenadas = 1, 2, 3  # atribuição multipla
x, y, x = coordenadas  # desempacotamento
```

Isto também é bastante útil em funções pois elas podem retornar tuplas.

```python
def nome_da_funcao():
    return 1, 2, 3  # tupla

x, y, z = nome_da_funcao()
```

E também podemos usar o **desempacotamento** para passar argumentos para funções, neste caso usamos um `*` para forçar o desempacotamento.

```python
triangulo = (3, 4, 5)
area = heron(*triangulo)  # desempacotamento das posições da tupla
print(f"A area do triangulo é {area}")
```

E o mesmo funciona quando os valores estão em um dicionário.

```python
triangulo = {'a': 3, 'b': 4, 'c': 5}
area = heron(**triangulo)  # desempacotamento dos valores do dicionário
print(f"A area do triangulo é {area}")

```