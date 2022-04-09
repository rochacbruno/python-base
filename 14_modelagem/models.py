import json
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from dundie.database import connect
from dundie.utils.email import check_valid_email


class Serializable(ABC):
    def dict(self):
        return vars(self)


@dataclass
class Person(Serializable):
    pk: str
    name: str
    dept: str
    role: str

    def __post_init__(self):
        if not check_valid_email(self.pk):
            raise RuntimeError("Email is Invalid")


@dataclass
class Balance(Serializable):
    person: Person
    value: Decimal

    def dict(self):
        return {"person": self.person.pk, "value": str(self.value)}


@dataclass
class Movement(Serializable):
    person: Person
    date: datetime
    actor: str
    value: Decimal


db = connect()

people = []
for pk, data in db["people"].items():
    people.append(Person(pk, **data))


person = people[0]
print(person.dict())

print(json.dumps(person.dict()))

balance = Balance(person=person, value=Decimal(100))
print(json.dumps(balance.dict()))
