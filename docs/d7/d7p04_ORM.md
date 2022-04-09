# ORM

Object Relational Mappers são ferramentas para mapear tabelas do banco de
dados e seus relacionamentos em classes e objetos.

Existe um grande número de ORMs existentes para trabalhar com SQL em Python
sendo os mais famosos o Django ORM (embutido no framework Django) e o
SQLAlchemy.

O SQLAlchemy é o ORM mais utilizado em projetos Python, é um projeto muito
robusto e bastante estabelecido e possui muitas funcionalidades.

Definindo Models com SQLAlchemy:

> **NOTA** como a biblioteca é bastante antiga e estável ainda não tem
> suporte nativo ao Python Moderno com type annotations e por isso
> precisamos utilizar classes normais e descritores especificos para os campos.

```py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Precisamos de uma classe base do sqlalchemy para criar models
# obtemos esta classe atráves de uma factory function
Base = declarative_base()


# Criamos nosso primeiro model
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))


# Criamos a conexão com o banco de dados
engine = create_engine("sqlite:///sqla_example.db")


# Pedimos ao SQLA para criar as tabelas caso não existam
Base.metadata.create_all(bind=engine)
```

Agora já pode abrir o `sqla_example.db` na extensão SQLite do Vscode ou no seu
client sqlite preferido e a tabela `person` estará criada.

O próximo passo para manipular e consultar dados é criar uma `Session`, a Session
é a classe responsável por criar cursores de dados, executar instruções e garantir
transações.

```py
...
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
```

E agora podemos por exemplo adicionar um registro ao banco de dados.

```py
person = Person(name="Bruno")
session.add(person)
session.commit()
```

Para selecionar dados também utilizamos a session e o método query

```py
results = session.query(Person).filter(Person.name == "Bruno")
for result in results:
    print(result.name)
```

O SQLALchemy é excelente e robusto, com ele é possível efetuar todo tipo de
operação SQL através de classes, como por exemplo joins.

Vamos criar uma outra tabela e adicionar alguns dados.
```py
...
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship('Person', foreign_keys='Balance.person_id')
```

- Usamos `ForeignKey` para marcar um campo como chave estrangeira
- Usamos `relationship` para criar uam referencia dinâmica entre as tabelas

Exemplo de uso:

```py
# Inserimos um registro na tabela com relacionamento
balance = Balance(value=100, person_id=person.id)
session.add(balance)
session.commit()
```

E agora podemos efetuar queries com `join`

```py
results = session.query(Person.name, Balance.value).join(Balance, isouter=True)
for result in results:
    print(result)
```

O retorno da query acima é uma tupla `("Bruno", 100)`

Podemos também usar as relationships definidas.

```py
results = session.query(Balance)
for result in results:
    print(result.person.name, result.value)
```

No caso acima acessamos a property `person` do objeto `Balance` e esta
property é uma referência relacional ao modelo `Person`.

## Conclusão

O SQLAlchemy é realmente poderoso e simples de usar mas é preciso entender
bastante a sua composição de objetos para conseguir efetuar consultas.

Por isso veremos na próxima aula como utilizar uma abstração em cima do SQLAlchemy
para facilitar e aplicar os conceitos de tipagem do Python 3+.


## Código completo

```py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# Precisamos de uma classe base do sqlalchemy para criar models
# obtemos esta classe atráves de uma factory function
Base = declarative_base()


# Criamos nosso primeiro model
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))


class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship('Person', foreign_keys='Balance.person_id')


# Criamos a conexão com o banco de dados
engine = create_engine("sqlite:///sqla_example.db")


# Pedimos ao SQLA para criar as tabelas caso não existam
Base.metadata.create_all(bind=engine)


# Criamos uma Session para manipular e consultar dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


# Agora podemos adicionar dados no banco de dados
person = Person(name="Bruno")
session.add(person)
session.commit()

# Inserimos um registro na tabela com relacionamento
balance = Balance(value=100, person_id=person.id)
session.add(balance)
session.commit()

# Para selecionar dados também utilizamos a session
# e a função query
results = session.query(Person).filter(Person.name == "Bruno")
for result in results:
    print(result.name)

# Efetuamos uma query com join
results = session.query(Person.name, Balance.value).join(Balance, isouter=True)
for result in results:
    print(result)

# Usando relationships
results = session.query(Balance)
for result in results:
    print(result.person.name, result.value)
```
