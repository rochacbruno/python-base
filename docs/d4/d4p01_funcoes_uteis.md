# Funções incluídas no Python

Funções são uma maneira de definir um bloco de código que pode ser reutilizado diversas vezes.

Python vem com uma grande quantidade de funções úteis e estão divididas entre as **builtin** (embutidas) e as
das **stdlib** (biblioteca padrão instalada junto com o Python)

## Funções builtin úteis

Python já vem com uma série de funções úteis https://docs.python.org/3/library/functions.html

### SUM

Obtem a soma dos elementos de um iterável contendo números

```py
>>> sum([1, 2, 3])
6
```

### MAX

Retorna o item com maior valor em uma sequência

```py
>>> max([1, 2, 3])
3
```

### MIN

Retorna o item com menor valor em uma sequência

```py
>>> min([1, 2, 3])
1
```

### LEN

Retorna o tamanho de uma sequência

```py
>>> len([1, 2, 3])
3
>>> len("Bruno")
5
```

### Reversed

Retorna uma sequência invertida

```py
>>> list(reversed([1, 2, 3]))
[3, 2, 1]
```

### Sorted

Retorna uma sequência ordenada alfabeticamente

```py
>>> list(sorted([9, 8, 1, 2, 3]))
[1, 2, 3, 8, 9]
```

### Filter

Aplica um filtro em uma sequência, sendo que o filtro é uma função que deve retornar True ou False

```py
>>> list(filter(str.isdigit, "Bruno987Rocha452"))
['9', '8', '7', '4', '5', '2']
```

### MAP

Aplica uma função de transformação em cima de uma sequência

```py
>>> list(map(str.upper, ["bruno", "rocha"]))
['BRUNO', 'ROCHA']
```

### All

Retorna `True` se todos os elementos da sequência forem avaliados para True

```py
>>> valores = [True, True, False]
>>> all(valores)
False
```
> **Atenção**: `all([])` é `True`

### Any


Retorna True se pelo menos um elemento da lista for avaliada para True

```py
>>> valores = [True, True, False]
>>> any(valores)
True
```

### Enumerate

Retorna um objeto iteravél que fornece a numeração de itens de uma sequência

```py
>>> nomes = ["Bruno", "Joao", "Maria", "Sofia"]

>>> for num, nome in enumerate(nomes):
...     print(num, nome)
0 Bruno
1 Joao
2 Maria
3 Sofia

>>> for num, nome in enumerate(nomes, start=5):
...     print(num, nome)
5 Bruno
6 Joao
7 Maria
8 Sofia

```

### ZIP

Junta 2 sequências em pares

```py
>>> colunas = ["nome", "sobrenome"]
>>> dados = ["Bruno", "Rocha"]

>>> zip(colunas, dados)
Out[38]: <zip at 0x7fa4c570ba00>

>>> list(zip(colunas, dados))
[('nome', 'Bruno'), ('sobrenome', 'Rocha')]

>>> dict(zip(colunas, dados))
{'nome': 'Bruno', 'sobrenome': 'Rocha'}

```

---

## Funções da std lib

Algumas funções estão incluídas mas precisam ser importadas.

### Random

Retorna elementos randomicos

```py
>>> import random

>>> random.random()
0.3416667413859049

>>> random.randint(1, 10)
8
>>> random.randint(1, 10)
4

>>> random.choice(["red", "green", "blue"])
'red'
>>> random.choice(["red", "green", "blue"])
'blue'


>>> random.sample([1, 2, 3, 4, 5], 2)
[4, 5]
>>> random.sample([1, 2, 3, 4, 5], 2)
[1, 3]

>>> numbers = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(numbers)
>>> numbers
[5, 2, 4, 6, 1, 3]
```

### Itertools

Funções úteis para trabalhar com objetos iteráveis

```py
>>> import itertools as it
>>> for item in it.cycle("ABCD"):
...     print(item)

>>> list(it.repeat("Bruno", 10))
['Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno']

>>> list(it.accumulate([1, 2, 3, 4, 5]))
[1, 3, 6, 10, 15]

>>> list(it.product("ABC", repeat=2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

>>> list(it.permutations("ABC"))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

>>> list(it.combinations("ABCDE", 2))
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

```

### Functools

Funções uteís para manipular funções

```py
>>> import functools as ft
>>> print("Bruno", "Rocha")
Bruno Rocha
>>> myprint = ft.partial(print, sep="---")
>>> myprint("Bruno", "Rocha")
Bruno---Rocha
```

### Statistics

Retorna estatisticas como por exemplo média e mediana.

```py
>>> import statistics as st
>>> st.mean([1, 2, 2, 5, 10, 12])
5.333333333333333
>>> st.median([1, 2, 2, 5, 10, 12])
3.5
```

### UUID

Universal Unique ID

```py
>>> import uuid
>>> uuid.uuid4()
UUID('db5601e3-5c7c-4fb0-91c4-60f33852e11c')
>>> str(uuid.uuid4())
'23b92cdb-f79f-41d9-a083-8474c02df541'
```

### getpass

Substitui o `input` ao ler passwords do terminal.

```py
>>> import getpass
>>> password = getpass.getpass()
Password: <invisible>
```

### SMTPLIB

Para enviar e-mails podemos usar a `smtplib`, esta biblioteca
permite o envio de mensagens formatadas no padrão SMTP.

Padrão SMTP:
```text
From: eu@server.com
To: destino@outroserver.com, outrodestino@server.com
Subject: Assunto do email

Mensagem do email a partir daqui
e em quantas linhas precisar.
```

Usamos Python para formatar a mensagem com interpolação:

```py
# setamos algumas constantes
SERVER = "localhost"
PORT = 8025
FROM = "eu@server.com"
TO = ["destino@outroserver.com", "outro@server.com"]
SUBJECT = "Assunto do e-mail"
TEXT = "Este é meu e-mail enviado via Python no terminal :)"

# interpolamos a mensagem
message = f"""\
From: {FROM}
To: {', '.join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

```

Para enviar essa mensagem de texto usando python criamos
uma instância do cliente SMTP

```py
import smtplib

with smtplib.SMTP(host=HOST, port=PORT) as server:
    server.sendmail(FROM, TO, message)
```

Antes de rodar o script precisamos ter um servidor de e-mails,
é possível se conectar a um servidor externo, como por exemplo o
do google com:

```py
server.starttls()
server.login(username, password)
```

Porém localmente você pode rodar um servidor de testes embutido no próprio Python, este servidor não envia e-mails, apenas imprime na tela para debugging.


Execute isso em um terminal:

```bash
python -m smtpd -c DebuggingServer -n localhost:8025
```

Deixe o comando acima rodando e em outro terminal:

`email.py`
```py
import smtplib

# setamos algumas constantes
SERVER = "localhost"
PORT = 8025
FROM = "eu@server.com"
TO = ["destino@outroserver.com", "outro@server.com"]
SUBJECT = "Assunto do e-mail"
TEXT = "Este é meu e-mail enviado via Python no terminal :)"

# interpolamos a mensagem
message = f"""\
From: {FROM}
To: {', '.join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
```

```bash
python email.py
```

e no outro terminal onde o e-mail server está rodando verá:

```bash
---------- MESSAGE FOLLOWS ----------
b'From: eu@server.com'
b'To: destino@outroserver.com, outro@server.com'
b'Subject: Assunto do e-mail'
b'X-Peer: ::1'
b''
b'Este \xc3\xa9 meu e-mail enviado via Python no terminal :)'
------------ END MESSAGE ------------
```

para enviar e-mails contendo Rich Text precisamos usar
um envelope do tipo MIMEText, nosso e-mail ficaria

```py
import smtplib
from email.mime.text import MIMEText

# setamos algumas constantes
SERVER = "localhost"
PORT = 8025
FROM = "eu@server.com"
TO = ["destino@outroserver.com", "outro@server.com"]
SUBJECT = "Assunto do e-mail"
TEXT = "Este é meu e-mail enviado via Python no terminal :)"

message = MIMEText(TEXT)
message["Subject"] = SUBJECT
message["From"] = FROM
message["To"] = ", ".join(TO)

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.as_string())
```

O output no servidor será:

```bash
---------- MESSAGE FOLLOWS ----------
b'Content-Type: text/plain; charset="utf-8"'
b'MIME-Version: 1.0'
b'Content-Transfer-Encoding: base64'
b'Subject: Assunto do e-mail'
b'From: eu@server.com'
b'To: destino@outroserver.com, outro@server.com'
b'X-Peer: ::1'
b''
b'RXN0ZSDDqSBtZXUgZS1tYWlsIGVudmlhZG8gdmlhIFB5dGhvbiBubyB0ZXJtaW5hbCA6KQ=='
------------ END MESSAGE ------------

```

A vantagem de usar MIMEText é que evitamos a interpolação de string e automaticamente
já será enviado como utf-8, além de que o conteúdo da mensagem será codificado em base64

Caso a mensagem contenha formatação HTML pode alterar `MIMEText(TEXT, "html")`

#### Usando mailtrap.io

Façá login em mailtrap.io e altere as informações de login para as suas próprias
disponíveis em show credentials na pagina principal da sua inbox.


```py
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(user="83f1618af77272", password="ff77c56ae6ef22")
    server.sendmail(FROM, TO, message.as_string())
```

Agora os e-mails serão enviados para a caixa de mensagens da mailtrap.io