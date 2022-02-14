### Textos

#### Caracteres

Agora sim vamos falar do último dos 4 tipos primários que abordaremos que é
o tipo usado para armazenar texto.

Tudo o que você aprendeu até agora sobre protocolos e métodos especiais também
se aplica aos textos, mas os textos tem uma pequena particularidade, eles
são formados por caracteres.

```py
>>> chr(65)
A
>>> chr(66)
B
>>> chr(67)
C
```

Portanto o texto `"ABC"` internamente contém um conjunto de 3 caracteres em suas
respectivas posições na tabela de caracteres.

Existem várias tabelas de caracteres usadas na computação mas nesse treinamento
vamos ficar em apenas duas `ascii` e `utf8`.

A tabela `ASCII` possui 128 posições, ou seja, vai do 0 ao 127 e em cada posição
armazena apenas um caracter.


![](./imgs/ascii.png)

Estes são os carecteres básicos da lingua inglesa e como pode perceber ela não
considera acentuação ou carecteres especiais de outros idiomas como Russo ou 
Mandarim.

Quando a computação globalizou foi preciso mudar de tabela e adotar uma maior que
pudesse comportar uma quantidade universal de caracteres e também os `emojis` que
se tornaram parte da comunicação moderna.

A tabela `unicode` de `8 bits` - **utf8** atualmente tem 120 mil caracteres.

https://unicode-table.com/en/

Nesta tabela além da tabela ASCII padrão, apartir da posição `128` temos acentuação
e sub tabelas para simbolos e emojis.

Na tabela `ASCII` cada caracter ocupava menos de 1 byte (7 bits) e por isso que
`A` é `65` que na tabela é `1000001` (7 digitos).

Já na tabela unicode cada caractere pode ser formado por mais de um byte, por
exemplo, uma letra com acento `Ã` ocupa 2 bytes `11000011 10000011` na tabela.

E alguns emojis como o 🍉 ocupam 4 bytes `11110000 10011111 10001101 10001001`

Durante a programação com Python nós iremos considerar que nossos textos 
utilizam os caracteres disponíveis na tabela `utf8` e em alguns raros casos
no Python3 teremos que explicitamente fazer operações de `encode` e `decode` a
partir de um texto `ascii` para `utf-8`.

```py
# variável
fruit = "🍉"

# para transmitir este texto ou gravar em um arquvivo
# ou banco de dados pode ser necessário encodificar ele.
>>> fruit.encode("utf-8")
b'\xf0\x9f\x8d\x89'
```

Esse valor `b'\xf0\x9f\x8d\x89'` é um objeto do tipo `bytes` e repare que ele
tem 4 elementos separados por `\` cada um deles é um dos bytes que formam a 🍉

A operação contrária, por exemplo quando lermos de um arquivo ou banco de 
dados que não suporta `utf8` será com o `decode`.

```py
melancia_em_bytes = b'\xf0\x9f\x8d\x89'
>>>  melancia_em_bytes.decode("utf-8")
'🍉'
```

O objeto ali iniciado por `b''` é uma sequencia de bytes em formato hexadecimal
a titulo de curiosidade

- f0 = 11110000 
- 9f = 10011111 
- 8d = 10001101 
- 89 = 10001001

Que são os 4 bytes que formam o carecte 🍉 e você pode verificar isso no Python
com cada um dos valores da lista:

```py
>>> hex(0b11110000)
'0xf0'
```

Em Python números começados com `0b` são binários e `0x` são hexadecimais.

#### Strings, ou cadeia de caracteres

Até aqui falamos de caracteres isolados como `A`, `B`, `🍉` mas ao programar
também precisaremos juntar esses carecteres para formar palavras e frases,
quando criamos uma variável do tipo texto em Python ele através da presença
de aspas sejam elas simples `'` ou duplas `"` armazena esse valor em uma classe
do tipo `str` e este tipo de dado pode armazenar um ou mais caracteres.

```py
>>> nome = "Bruno"
type(nome)
```

E como você já deve ter imaginado aqui estamos armazenando cada uma das letras
`B`, `r`, `u`, `n`, `o` com seus respectivos bytes e sequencia posicional em um
único objeto. (a plavra string significa corda, cadeia ou corrente),

A palavra `"Bruno"` é uma lista contendo em cada posição um caractere da tabela
`utf8`.

```py
>>> list(bytes(nome, "utf-8"))
[66, 114, 117, 110, 111]

>>> chr(66)
'B'

>>> chr(114)
'r'

>>> chr(117)
'u'

>>> chr(110)
'n'

>>> chr(111)
'o'
```

Bem, para guardar o nome "Bruno" você mais uma vez não precisa se procupar com
esses detalhes todos, basta fazer `nome = "Bruno"` e usar este texto para efetuar
as operações que você desejar, porém é muito útil saber como o objeto está
implementado pois isso te permite efetuar operações como a que fizemos em 
nosso script `hello.py`

```py
current_language = os.getenv("LANG", "en_US")[:5]
```

Sabendo que `current_language` poderia ter o valor `en_US.utf8` nós usamos
o protocolo `Sliceable` do objeto `str` para **fatiar** o texto e pegar
somente os primeiros 5 caracteres.

```py
>>> "en_US.utf8"[:5]
'en_US'

>>> "Bruno"[2]
'u'

>>> "Python"[0]
'P'
```

O tipo `str` possui a maioria das carecteristicas que já abordamos nos outros
tipos de dados e uma grande quantidade de protocolos implementados, vamos ver
alguns.

```py
# Sliceable (pode ser fatiado)
>>> "Bruno"[1]
'r'
# que internamente invoca o método `__getitem__`
>>> "Bruno".__getitem__(1)
'r'

# Addible (pode ser adicionado a outro texto)
# Essa operação se chama "Concatenação"
>>> nome = Bruno" 
>>> sobrenome = "Rocha"
>>> nome + " " + sobrenome
'Bruno Rocha'
# que internamente invoca o método `__add__`
>>> nome.__add__(" ".__add__(sobrenome))
'Bruno Rocha'

# Multipliable (que pode ser multiplicado)
>>> "Bruno" * 5
'BrunoBrunoBrunoBrunoBruno'

# Iterable (que pode ser iterado/percorrido)
>>> for letra in "Bruno":
...     print("-->" + letra.upper())
-->B
-->R
-->U
-->N
-->O
# Internamente o statement `for` invoca o método `__iter__`
>>> iterador = "Bruno".__iter__()
>>> next(iterador)
'B'
>>> next(iterador)
'r'
```

Além disso tudo, o tipo `str` também oferece muitos métodos públicos, que nós
podemos usar explicitamente e que são muito úteis.

```py
>>> "Bruno".upper()
'BRUNO'

>>> "BRUNO".lower()
'bruno'

>>> "bruno rocha".capitalize()
'Bruno rocha'

>>> "bruno rocha".title()
'Bruno Rocha'

>>> "bruno rocha".split(" ")
['bruno', 'rocha']

>>> "bruno".startswith("b")
True

>>> "bruno".endswith("b")
False

>>> "bruno rocha".count("o")
2

>>> "bruno rocha".index("c")
8
>>> "bruno rocha"[8]
'c'
```

E também algumas coisas que podemos fazer com qualquer objeto sequencial do
Python:

```py
>>> len("Bruno Rocha")
11

>>> sorted("Bruno Rocha")
[' ', 'B', 'R', 'a', 'c', 'h', 'n', 'o', 'o', 'r', 'u']

>>> list(reversed("Bruno Rocha"))
['a', 'h', 'c', 'o', 'R', ' ', 'o', 'n', 'u', 'r', 'B']
```

#### Interpolação e Formatação de textos

Uma das coisas mais úteis de se fazer com texto é a interpolação de variáveis
dentro do texto e a formatação de acordo com template pre-definido.

**Interpolação** é uma alternativa a **concatenação**, enquanto a concatenação
usa o sinal de `+` como em `"Bruno" + "Rocha"` na interpolação usamos templates
com posicionamento.

Python oferece 3 maneiras de fazer **Interpolação**, a primeira e mais antiga 
delas segue um padrão universal adotado em muitos sistemas e em outras linguagens
de programação e utiliza o sinal de `%` como marcador de template.

##### %

```py
>>> mensagem = "Olá %s, você é o participante número %d e pode ganhar %f pontos."
>>> nome = "Bruno"
>>> numero = 4
>>> pontos = 42.5
>>> print(mensagem % (nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.500000 pontos.
```

Este tipo de formatação usa o `%` acompanhado de `s` para str, `d` para int, ou
`f` para float, e além de demarcar o **placeholder** onde a substituição irá
ocorrer também podemos definir a precisão numérica como em `%.2f` que significa
que queremos imprimir apenas 2 casas decimais do número float.

```py
>>> mensagem = "Olá %s, você é o participante número %d e pode ganhar %.2f pontos."
>>> print(mensagem % (nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.50 pontos.
```

E também é possivel utilizar parâmetros nomeados.

```py
>>> mensagem = "Olá %(nome)s, você é o participante número %(num)d e pode ganhar %(pon).2f pontos."
>>> print(mensagem % {"nome": "Bruno", "num": 4, "pon": 42.5})
Olá Bruno, você é o participante número 4 e pode ganhar 42.50 pontos.
```


Apesar do uso de `%` ter caido em desuso no Python3, ainda existem bibliotecas
como a `logging` que ainda utiliza este formato.

##### format

Esta é a forma preferida para fazer interpolação de textos pois além
de permitir a substituição de variáveis também permite a formatação
dos valores, vejamos alguns exemplos:

```py
>>> mensagem = "Olá {}, você é o participante número {} e pode ganhar {} pontos."
>>> print(mensagem.format(nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.5 pontos.
```

Repare que ao invés de `%` agora usamos `{}` para marcar um **placeholder**
e ao inves de `%` usamos a chamada do método `.format` do próprio tipo `str`
para passar os valores em sequência.

E também podemos especificar tipos e a precisão numérica usando `:` e os mesmos
marcadores dentro de `{}`.

```py
>>> mensagem = "Olá {:s}, você é o participante número {:d} e pode ganhar {:.2f} pontos."
>>> print(mensagem.format(nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.50 pontos.
```

Podemos utilizar outras opções de formatação em cada uma das marcações entre `{}`.
existe toda uma mini linguagem de formatação:

```py
{[[fill]align][sign][#][0][width][grouping_option][.precision][type]}
```

```
fill - <any charac­ter>
align - "­<" | "­>" | "­=" | "­^"
sign - "­+" | "­-" | " "
width - digit+
grouping_option - "­_" | "­,"
precision - digit+
type - "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

Exemplos:

```py
# Centralizar fazendo ocupar exatamente 11 caracteres.
>>> "{:^11}".format("Bruno")
'   Bruno   '

# A mesma coisa porém alinhado à direita.
>>> "{:>11}".format("Bruno")
'      Bruno'

# Agora preenchendo os espaços com outro carectere
>>> "{:*^11}".format("Bruno")
'***Bruno***'

# Definindo tipo e precisão para números
>>> "{:*^11.2f}".format(45.30000041)
'***45.30***'

```

O site Pyformat https://pyformat.info/ oferece um guia bastante intuitivo
para utilizar as opções de formatação, elas são tantas que não daria para
abordarmos todas elas neste treinamento, mas não se preocupe que durante os
nossos exercícios vamos utilizar as mais comuns.

##### f strings

No Python 3 foi introduzido um atalho bastante útil para usar o `format` e de
uma forma mais natural agora podemos escrever strings que se auto formatam
usando as variáveis existentes, o funcionamento respeita as mesmas opções
vistas anteriormente, o que muda é só a forma de escrever, ao invés de chamar
explicitamente `.format()` usamos `f"texto"`.

```py
# Texto
>>> nome = "Bruno"
>>> f"{nome:*^11}"
'***Bruno***

# Número
>>> valor = 45.30000041
>>> f"{valor:*^11.2f}"
'***45.30***'
```

Uma útilidade interessante das f-strings é usar para fazer debugging.

```py
>>> nome = "Bruno"
>>> print(f"{nome=}")
nome='Bruno'
```

Durante o treinamento usaremos:

- `%s` para logs
- `.format` para templates salvos, por exemplo para enviar e-mails
- `f-string` para todas as outras mensagens do programa
