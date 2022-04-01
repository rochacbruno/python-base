# Python data Model e Protocolos

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


