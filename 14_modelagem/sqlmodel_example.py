from typing import List, Optional

from sqlmodel import (
    Field,
    Relationship,
    Session,
    SQLModel,
    create_engine,
    select,
)


# We have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issues/189
from sqlmodel.sql.expression import Select, SelectOfScalar
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


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


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    person_id: int = Field(foreign_key="person.id")

    person: Person = Relationship(back_populates="balance")


engine = create_engine("sqlite:///sqlmodel_example.db", echo=False)
SQLModel.metadata.create_all(bind=engine)


with Session(engine) as session:
    person = Person(name="Bruno")
    session.add(person)

    balance = Balance(value=100, person=person)
    session.add(balance)

    session.commit()


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


with Session(engine) as session:
    for name in ["Sales", "Engineering", "Quality"]:
        session.add(Dept(name=name))
    session.commit()


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


with Session(engine) as session:
    person = session.exec(select(Person).where(Person.name == "Jim")).first()
    print(f"Departments of {person.name}", person.depts, sep="\n")

    sales = session.exec(select(Dept).where(Dept.name == "Sales")).first()
    print(f"People on {sales.name}", sales.people, sep="\n")
