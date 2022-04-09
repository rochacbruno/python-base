# SQLModel

O SQLAlchemy como vimos é excelente mas em alguns casos bastante complicado
e além disso o SQLAlchemy ainda não entende nativamente as type annotations.

Existe porém uma biblioteca criada para facilitar o uso do SQLAlchemy,
o SQLModel utiliza type annotations para a definição de models assim como
fizemos com `dataclass` e `Pydantic` e abstrai bastante da complexidade do
SQLAlchemy mantendo a compatibilidade com todos os recursos.


Repetindo o mesmo exemplo anterior usando SQLModel.


```py
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, select


# Definimos os modelos de dados usando type annotations
class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    balance: "Balance" = Relationship(back_populates="person")


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    person_id: int = Field(foreign_key="person.id")

    person: Person = Relationship(back_populates="balance")


# criamos a conexão e o banco de dados
engine = create_engine("sqlite:///sqlmodel_example.db", echo=False)
SQLModel.metadata.create_all(bind=engine)

# usamos a session como um context manager

with Session(engine) as session:
    person = Person(name="Bruno")
    session.add(person)

    balance = Balance(value=100, person=person)
    session.add(balance)

    session.commit()


# Manipulamos dados usando a session e o método exec em conjunto com select

with Session(engine) as session:

    # select simples
    sql = select(Person)
    person = session.exec(sql).first()
    print(person)

    # com condicional
    sql = select(Person).where(Person.name == "Bruno")
    person = session.exec(sql).first()
    print(person)
    print(person.balance[0])

    # utilizando referencia
    sql = select(Balance).where(person == person)
    balance = session.exec(sql).first()
    print(balance)
    print(balance.person.name)

    # join explicito
    sql = select(Person, Balance).where(Balance.person_id == Person.id)
    results = session.exec(sql)
    for person, balance in results:
        print(person.name, balance.value)

    # outer join (usando foreign keys)
    sql = select(Person, Balance).join(Balance, isouter=True)
    results = session.exec(sql)
    for person, balance in results:
        print(person.name, balance.value)
```

## Many to Many relationships

As vezes precisamos criar relacionamentos que não são 1 para 1, ou seja,
imagine que temos uma lista de departamentos na empresa e que um funcionário
possa fazer parte de mais de um departamento.

Para esses casos precisamos criar uma relação `Many to many` (muitos para muitos)
e o jeito de fazer isso é criando uma tabela de apoio chamada de `link table`.


Usando o mesmo exemplo anterior.

```py
class PersonDeptLink(SQLModel, table=True):
    dept_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="dept.id"
    )
    person_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="person.id"
    )


class Dept(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    people: List["Person"] = Relationship(
        back_populates="depts", link_model=PersonDeptLink
    )


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    balance: "Balance" = Relationship(back_populates="person")

    depts: List[Dept] = Relationship(
        back_populates="people", link_model=PersonDeptLink
    )
```

Agora podemos criar alguns departamentos:

```py
with Session(engine) as session:
    for name in ["Sales", "Engineering", "Quality"]:
        session.add(Dept(name=name))
    session.commit()
```

E os registros serão criados:
```text
id	name
1	Sales
2	Engineering
3	Quality
```

Agora podemos adicionar um funcionário que faz parte de 2 departamentos.

```py
with Session(engine) as session:
    sales = session.exec(select(Dept).where(Dept.name == "Sales")).first()
    quality = session.exec(select(Dept).where(Dept.name == "Quality")).first()

    person = Person(
        name="Jim",
        balance=[Balance(value=100)],
        depts=[sales, quality]
    )
    session.add(person)
    session.commit()
```

Esta será nossa link table

```
dept_id	person_id
1	1
3	1
```

> O funcionário `1` faz parte dos depts `1` e `3`

```py
with Session(engine) as session:
    person = session.exec(select(Person).where(Person.name == "Jim")).first()
    print(f"Departments of {person.name}", person.depts, sep="\n")

    sales = session.exec(select(Dept).where(Dept.name == "Sales")).first()
    print(f"People on {sales.name}", sales.people, sep="\n")
```

Resultado:

```bash
Departments of Jim
[Dept(name='Sales', id=1), Dept(name='Quality', id=3)]
People on Sales
[Person(name='Jim', id=1, depts=[Dept(name='Sales', id=1, people=[...]), Dept(name='Quality', id=3)])]
```


Agora vamos na próxima aula implementar o SQLModel em nosso projeto dundie.


## IMPORTANTE

Para evitar warnings do SQLAlchemy precisamos aplicar um patch no topo do
arquivo.

```py
# We have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issues/189
from sqlmodel.sql.expression import Select, SelectOfScalar
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
```
