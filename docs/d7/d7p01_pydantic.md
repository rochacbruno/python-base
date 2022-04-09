# Day 7 - Part 1 - modelagem com Dataclass e Pydantic

> **NOTA** O código antes das alterações desta aula está em [https://github.com/rochacbruno/dundie-rewards/tree/before_pydantic](https://github.com/rochacbruno/dundie-rewards/tree/before_pydantic)

Data classes são excelentes para representar objetos que armazenam dados,
vamos voltar ao nosso projeto `dundie` e ver onde podemos usar uma dataclass.

Criamos um arquivo `dundie/models.py` e nele vamos modelar o esquema do banco de
dados usando DataClass.

Transformamos as tabelas definidas em `database.json` em uma modelagem como:

```python
from decimal import Decimal
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    pk: str
    name: str
    dept: str
    role: str


@dataclass
class Balance:
    person: Person
    value: Decimal


@dataclass
class Movement:
    person: Person
    date: datetime
    actor: str
    value: Decimal
```

E podemos fazer o processo de de-serialização (ler os dados do JSON e a partir deles criar instâncias de objetos)

```python
from dundie.database import connect
db = connect()

people = []
for pk, data in db["people"].items():
    people.append(Person(pk, **data))

print(people[0])
```

O que acontece se tivermos um e-mail inválido no JSON?

```json
"people": {
        "jim@": {
            "name": "Jim Halpert",
            "dept": "Sales",
            "role": "Salesman"
        },
```

Ao executarmos obtemos

```python
Person(pk='jim@', name='Jim Halpert', dept='Sales', role='Salesman')
```

Uma das vantagens de usar modelagem de dados é a possibilidade de adicionar validação,
em dataclasses a validação pode ser feita no método `__post_init__`

```python
from dundie.utils.email import check_valid_email

class InvalidEmailError(Exception):
    ...


@dataclass
class Person:
    pk: str
    name: str
    dept: str
    role: str

    def __post_init__(self):
        if not check_valid_email(self.pk):
            raise InvalidEmailError("Email is Invalid")

    def __str__(self):
        return f"{self.name} - {self.role}"

```

```python
Traceback (most recent call last):
RuntimeError: Email is Invalid
```

E agora se quisermos ter os dados de uma instância de volta ao formato JSON?

```python
import json

person = people[0]
print(vars(person))
```
```python
# Built-in vars() get a dictionary from a class
{'pk': 'jim@dundlermifflin.com', 'name': 'Jim Halpert', 'dept': 'Sales', 'role': 'Salesman'}

# And json.dumps converte para JSON em string
print(json.dumps(vars(person)))
{"pk": "jim@dundlermifflin.com", "name": "Jim Halpert", "dept": "Sales", "role": "Salesman"}
```

Até aqui tudo bem, mas e se quisermos fazer isso com uma instância de `Balance` ?

```python
balance = Balance(person=person, value=Decimal(100))
print(json.dumps(vars(balance)))
TypeError: Object of type Person is not JSON serializable
```

Neste caso será necessário criarmos uma classe base capaz de serializar nossos
objetos para dicionário.


```python=
class Serializable(ABC):
    def dict(self):
        return vars(self)

@dataclass
class Person(Serializable):
    ...

@dataclass
class Balance(Serializable):
    ...


@dataclass
class Movement(Serializable):
    ...
```

No entando vai funcionar perfeitamente em `Person` mas ainda não em `Balance`

```python
print(person.dict())

print(json.dumps(person.dict()))

balance = Balance(person=person, value=Decimal(100))
print(json.dumps(balance.dict()))
TypeError: Object of type Person is not JSON serializable
```

Precisamos customizar o método `dict` na classe `Balance`

```python
@dataclass
class Balance(Serializable):
    person: Person
    value: Decimal

    def dict(self):
        return {
            "person": self.person.pk,
            "value": str(self.value)
        }
```

```python
balance = Balance(person=person, value=Decimal(100))
print(json.dumps(balance.dict()))
```
```python
{"person": "jim@dundlermifflin.com", "value": "100"}
```

É um pouco trabalhoso mas funciona, agora temos como serializar e de-serializar nosso
banco de dados em JSON para objetos e vice-versa, isso pode funcionar da mesma maneira
para JSON lido a partir de uma API.


## Pydantic


Apesar de dataclasses serem uma boa solução na maioria dos casos, quando trabalhamos
com serialização de dados, validação e especialmente bancos de dados no Python Moderno
esse trabalho fica bem melhor usando a biblioteca [Pydantic](https://pydantic-docs.helpmanual.io/) que é totalmente baseada em type annotations.


```python
pip install pydantic
```

Agora vamos modelar a mesma solução usando `Pydantic`, ao invés de usarmos o
decorator `@dataclass` iremos criar nossos objetos derivando da classe `BaseModel`


```python
from pydantic import BaseModel

class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    def __str__(self):
        return f"{self.name} - {self.role}"


...
```

E podemos adicionar validação através de decorators:

```python
from pydantic import BaseModel, validator
from dundie.utils.email import check_valid_email

class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    ...
    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalidEmailError("Email is Invalid")
        return v

    def __str__(self):
        return f"{self.name} - {self.role}"

```

Podemos usar validators também para fazer transformações em valores de entrada:


```python
class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)  # executa antes de inicializat o objeto
    def value_logic(cls, v):
        return Decimal(v) * 2

```


E podemos efetuar serialização para Json direto no objeto:

```python

person = Person(
    pk="bruno@rocha.com", name="Bruno", dept="engineering", role="programmer"
)
balance = Balance(person=person, value=100)
print(balance.json())
```
```python
{"person": {"pk": "bruno@rocha.com", "name": "Bruno", "dept": "engineering", "role": "programmer"}, "value": 200}
```

E até customizar como referências são serializadas para JSON.


```python
class Balance(BaseModel):
    ...
    class Config:
        json_encoders = {Person: lambda p: p.pk}


person = Person(
    pk="bruno@rocha.com", name="Bruno", dept="engineering", role="programmer"
)
balance = Balance(person=person, value=100)
print(balance.json(models_as_dict=False))
```
```json
{"person": "bruno@rocha.com", "value": 200}
```

Código completo:


```python
from pydantic import BaseModel, validator, Field
from decimal import Decimal
from datetime import datetime
from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self):
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)
    def value_logic(cls, v):
        return Decimal(v) * 2

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class User(BaseModel):
    person: Person
    password: str = Field(default_factory=generate_simple_password)

    class Config:
        json_encoders = {Person: lambda p: p.pk}


if __name__ == "__main__":
    p = Person(pk="bruno@g.com", name="Bruno", dept="Sales", role="NA")
    print(p)
    print(p.json())

    b = Balance(person=p, value=100)
    print(b.json(models_as_dict=False))

    m = Movement(person=p, date=datetime.now(), actor="sys", value=10)
    print(m.json(models_as_dict=False))

    u = User(person=p)
    print(u.json(models_as_dict=False))
```

```bash
Bruno - NA
{"pk": "bruno@g.com", "name": "Bruno", "dept": "Sales", "role": "NA"}
{"person": "bruno@g.com", "value": 200}
{"person": "bruno@g.com", "date": "2022-04-06T09:56:07.527029", "actor": "sys", "value": 10}
```

Uma grande vantagem de usar Pydantic é que vamos poder usar os mesmos models para conectar com bancos de dados e também para criar APIs com FastAPI.
