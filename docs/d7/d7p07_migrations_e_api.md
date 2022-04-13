# Migrations e API Rest


> O código no inicio desta aula https://github.com/rochacbruno/dundie-rewards/tree/day7p07

```bash
git clone --branch day7p07 https://github.com/rochacbruno/dundie-rewards
# ou caso já tenha o repositório clonado
git pull https://github.com/rochacbruno/dundie-rewards day7p07
# ou caso tenha seu próprio repositótio ou fork
git remote add upstream https://github.com/rochacbruno/dundie-rewards
git fetch --all
git rebase upstream/day7p07
```

Agora vamos falar de 2 temas relacionados a consulta e armazenagem de dados

- Database migrations
- Requisições em API REST


## Migrations

Digamos que agora que o banco de dados já está modelado e em produção em nosso
projeto agora tenhamos que adicionar um novo campo na tabela de `Person`.

Poderiamos simplesmente executar a instrução SQL

```sql
ALTER TABLE person ADD column currency varchar;
```

depois adicionar o campo em `models.py`

```py
class Person(...):
    ...
    currency: str = Field(default="USD")
```

E tudo estaria OK para continuarmos trabalhando.

## Então qual o motivo de usar migrations?

Imagina agora que temos 10 pessoas programando no mesmo projeto e você
faz uma alteração dessas apenas no seu código, ou simplesmente
imagine que você agora precise executar esse comando SQL manualmente
em todos os bancos de dados onde o projeto está em produção, é invivável.

Por isso existe um padrão chamado de `migrations` que toda vez que precisamos
adicionar ou alterar estrutura de nossas tabelas automatizamos com as migrations.

## Alembic

Para o SQLAlchemy usamos a extensão `alembic`

```bash
pip install alembic
echo "alembic" >> requirements.txt
```

Agora vamos ao nosso projeto e rodamos

```bash
alembic init migrations
```

O alembic irá criar alguns arquivos:

- migrations/*  (environment do alembic)
- alembic.ini  (arquivo e configuração)


Começamos editando o `alembic.ini` para apontar para nosso banco de dados

```ini
# em torno da linha 55
sqlalchemy.url = sqlite:///assets/database.db
```

Agora editamos `migrations/script.py.mako` que é um template usado pelo alembic
para gerar os scripts que automatizam as alterações do banco de dados.

Precisamos informar ao alembic que usamos o SQLModel ao invés do SQLAlchemy puro.

```py
# em torno da linha 10
# (logo após) import sqlalchemy as sa
import sqlmodel
```


Alteramos `migrations/env.py` para informar os nossos models.


```py
# em torno da linha 8
# (logo após) from alembic import context
from dundie import models  # noqa

# em torno da linha 23
target_metadata = models.SQLModel.metadata
```

## Definindo a migration inicial

É uma boa prática criar uma migration inicial, um ponto de partida para o
histórico de alterações do nosso banco de dados.

```bash
alembic revision --autogenerate -m "initial"
```
```
Generating dundie-rewards/migrations/versions/4594b7879fd2_initial.py ...  done
```

Agora precisamos aplicar essa revisão em nosso banco de dados.

```bash
alembic upgrade head
```

Agora o alembic terá criado uma tabela chamada `alembic_version` no banco de dados
e ali vai armazenar o histórico de alterações e ordem dos scripts de migration.

Se precisarmos reverter algo podemos usar um dos comandos do `alembic`

## Alterando uma tabela

Agora podemos alterar o nosso model `Person` e adicionar o campo `currency` que
vai armazenar a moeda corrente da pessoa.

> Vamos usar essa informação para calcular a cotação usando uma API :)

`dundie/models.py`
```py
class Person(...):
    ...
    currency: str = Field(default="USD")
```

Ao invés de alterarmos o banco de dados diretamente usando SQL agora vamos
pedir para o `alembic` gerar um script de migration.

```bash
alembic revision --autogenerate -m "Adicionado campo currenty a person"
```
```
Generating dundie-rewards/migrations/versions/0fd9036f5d33_adicionado_campo_currenty_a_person.py ...  done
```

Este script vai conter as instruções necessárias para adicionar o campo na tabela
e a vantagem é que agora todas as outras pessoas que programam no mesmo projeto
também vão poder executar o alembic para ter seus bancos de dados atualizados
localmente. (e inclusive em produção)

Agora pedimos ao alembic para atualizar o banco de dados.

```bash
alembic upgrade head
```
```
Running upgrade 4594b7879fd2 -> 0fd9036f5d33, Adicionado campo currenty a person
```

Agora fazemos um commit no git e mandamos a migration para o repositório
assim todo mundo que está trabalhando poderá obter o mesmo resultado.

```
$ alembic history
4594b7879fd2 -> 0fd9036f5d33 (head), Adicionado campo currenty a person
<base> -> 4594b7879fd2, initial
```

> **DICA** podemos colocar esses comandos no `Makefile`


## Carregando dados do arquivo `people.csv`

Alteramos o arquivo `people.csv` adicionando `currency` como último campo.

```csv
Jim Halpert, Sales, Salesman, jim@dundlermifflin.com, USD
Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com, EUR
Gabe Lewis, C-Level, CEO, glewis@dundlermifflin.com, BRL
Pam Beasly, General, Receptionist, pam@dm.com, BRL
Bruno, General, Guard, bruno@dm.com, BRL
```

Alguns funcionários trabalham nos Estados Unidos, outros na Europa e tem
gente trabalhando remotamente no Brasil, portanto temos currencies diferentes.

Agora alteramos o `core.py:load`

```py
# linha 32
headers = ["name", "dept", "role", "email", "currency"]
...
```

E o `cli.py:load`

```py
# linha 43
headers = ["email", "name", "dept", "role", "currency", "created"]
```

E em `utils/db.py:add_person`

```py
# perto da linha 33
existing.currency = instance.currency

```

Agora podemos rodar o comando `load`

```bash
❯ dundie load ~/Projects/dundie-rewards/assets/people.csv
                                  Dunder Mifflin Associates
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃ email                      ┃ name           ┃ dept    ┃ role         ┃ currency ┃ created ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━┩
│ jim@dundlermifflin.com     │ Jim Halpert    │ Sales   │ Salesman     │ USD      │ False   │
│ schrute@dundlermifflin.com │ Dwight Schrute │ Sales   │ Manager      │ EUR      │ False   │
│ glewis@dundlermifflin.com  │ Gabe Lewis     │ C-Level │ CEO          │ BRL      │ False   │
│ pam@dm.com                 │ Pam Beasly     │ General │ Receptionist │ BRL      │ False   │
│ bruno@dm.com               │ Bruno          │ General │ Guard        │ BRL      │ False   │
└────────────────────────────┴────────────────┴─────────┴──────────────┴──────────┴─────────┘
```

Ao consultar no SQL também verá o campo `currency`

```sql
SELECT * FROM person;
id	email	name	dept	role	currency
1	jim@dundlermifflin.com	Jim Halpert	Sales	Salesman	USD
2	schrute@dundlermifflin.com	Dwight Schrute	Sales	Manager	EUR
3	glewis@dundlermifflin.com	Gabe Lewis	C-Level	CEO	BRL
4	pam@dm.com	Pam Beasly	General	Receptionist	BRL
5	bruno@dm.com	Bruno	General	Guard	BRL
```

## Consultando uma API REST para obter a cotação


O objetivo agora é usarmos uma API REST para integrar com nosso projeto.

Requerimento do projeto:

```text
Ao executar `dundie show` quero ser capaz de visualizar o valor a ser
pago em moeda corrente para cada funcionário.

Os funcionários poderão resgatar no final de cada ano o seu saldo de pontos
em dólar.

Cada ponto do dundie-rewards vale 1 dolar porém cada funcionário está em um
local do planeta e quero exibir na moeda corrente de cada um.
```

Usaremos a `https://economia.awesomeapi.com.br/json/last/USD-<CURRENCY>` para obter
a cotação do dia dependendo da `currency` configurada em cada pessoa.

`settings.py`
```py
API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/USD-{currency}"
```

Usaremos uma lib chamada `httpx` para se comunicar com a API

```bash
echo "httpx" >> requirements.txt
```

criamos um arquivo `utils/exchange.py` e criamos uma função `get_rates`


```py
import httpx
from decimal import Decimal
from typing import List, Dict
from dundie.settings import API_BASE_URL
from pydantic import BaseModel, Field


class USDRate(BaseModel):
    code: str = Field(default="USD")
    codein: str = Field(default="USD")
    name: str = Field(default="Dolar/Dolar")
    value: Decimal = Field(alias="high")


def get_rates(currencies: List[str]) -> Dict[str, USDRate]:
    """Gets the current rates of dolar in each currency"""
    return_data = {}
    for currency in currencies:
        if currency == "USD":
            return_data[currency] = USDRate(high=1)
        else:
            response = httpx.get(API_BASE_URL.format(currency=currency))
            if response.status_code == 200:
                data = response.json()["USD"]
                return_data[currency] = USDRate(**data)
            else:
                return_data[currency] = USDRate(name="Api/Error", high=0)
    return return_data
```


E agora usamos essa função para obter as currencies em nosso comando `show`
para isso alteramos o `core.py:read`

```py
from dundie.utils.exchange import get_rates

def read(....):
    ...
    with get_session() as session:
        # obtemos toda as currencies existentes ["BRL", "USD", "EUR"]
        currencies = session.exec(select(Person.currency).distinct(Person.currency))
        rates = get_rates(currencies)
        ...
        for person in results:
            total = rates[person.currency].value * person.balance[0].value
            return_data.append(
                ...
                **{"value": total}
            )
```

Agora podemos melhorar a formatação do campo no `cli.py`

```py
def show(...):
    ...
    for person in result:
        person["value"] = f"{person['value']:.2f}"
        person["balance"] = f"{person['balance']:.2f}"
        ...
```
