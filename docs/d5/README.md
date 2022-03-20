# Testes

No Day 5  o código e material está incluido no projeto https://github.com/rochacbruno/dundie-rewards


```py
# decorators
from functools import wraps

## Dobra

def dobra(f)
    @wraps(f)
    def modificador(a, b):
        return f(a * 2, b * 2)
    return modificador


## Aplicando o decorator
funcao = dobra(funcao)

## OU

@dobra
def soma(a, b):
    return a + b


assert soma(1, 2) == 6


## TExto HTML

def bold(f):
    @wraps(f)
    def wrapper(text):
        result = f(text)
        return f"<strong>{result}</strong>"
    return wrapper


def italic(f):
    @wraps(f)
    def wrapper(text):
        result = f(text)
        return f"<i>{result}</i>"
    return wrapper


@bold
@italic
def hello(text):
    return f"Hello {text}"


assert hello("Bruno") == '<i><strong>Hello Bruno</strong></i>'
```
