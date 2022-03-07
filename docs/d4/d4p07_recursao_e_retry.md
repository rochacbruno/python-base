# Paradigmas de programação

O paradigma de programação imperativo/procedural é o que usamos na maior parte do tempo
neste paradigma as instruções são definidas uma a uma e utilizamos alocação de variáveis
para manter o estado do programa.

No paradigma funcional usamos funções e a habilidade de podermos passar funções como 
argumentos para outras funções e também o uso de composição com chamadas recursivas
e evitamos ao máximo a alocação de variáveis para a funções não ter efeitos colaterais.

## Comparativo

```py
"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]

```


###  estilo funcional

```py
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")
```

### Estilo procedural / imperativo

```py
def starts_with_b(text):
    """Return bool if text starts with b"""
    return text[0].lower() == "b"


filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
```

## Retry

As vezes queremos tentar várias vezes executar uma tarefa sujeita a erros de maneira
que possamos customizar a quantidade de tentativas.

Isto é bastante útil em cenários onde dependemos de operações de I/O como leitura de
arquivos, servidores e serviços que precisam ser executados etc.


Neste script estamos abrindo um arquivo em modo leitura e lendo as suas 
linhas através do método `readlines()` que nos retorna uma lista contendo
cada uma das linhas do arquivo.

`cat errors.py`
```py
#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASk Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("names.txt").readlines()  # FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")
```

Porém, caso o arquivo não exista teremos um erro chamado `FileNotFoundError`

Logo após o `sys.exit(1)` nós colocamos um `TODO: Usar retry` e vamos agora desenvolver 
o retry.

### Retry com loop

A primeira forma de efetuar um retry é usando `loop`

- criamos uma função que tenta abrir o arquivo um certo número de tentativas
- chamamos essa função em nosso script

```py
#!/usr/bin/env python3
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to ASk Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)


def try_to_open_a_file(filepath, retry=1):
    for attempt in range(1, retry + 1):
        print(f"tentativa número {attempt}")
        try:
            return open(filepath).readline()
        except FileNotFoundError as e:
            log.error("ERRO %s", e)
            time.sleep(2)  
            # ^ isso aqui é só para fingir que estamos esperando um processo terminar
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
```

No código acima criamos uma função que podemos chamar passando o argumento `retry=5`
e esta função irá tentar abrir o arquivo 5 vezes antes de falhar.

### Retry com recursão

Recursão é quando uma função é capaz de invocar ela mesma para efetuar a repetição de seu 
próprio algoritmo.

Python não é uma linguagem otimizada para recursão e possui um limite de 1000 chamadas
portanto ao escrever funções recursivas precisamos nos atentar a validação deste limite
e entre outros cuidados está também o correto tratamento de exceptions e o correto
retorno do valor da função executada.

```py
#!/usr/bin/env python3
import time
import logging

log = logging.Logger("errors")


# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""
    if retry > 999:
        raise ValueError(
            "Retry cannot be above 999 because of Python recursion limit"
        )

    try:
        return open(filepath).readlines()  # FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            # recursão
            return try_to_open_a_file(filepath, retry=retry - 1)
    else:
        print("Sucesso!!!")
    finally:
        print("Execute isso sempre!")

    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
```