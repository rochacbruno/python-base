from datetime import datetime
from decimal import Decimal
from typing import Union
from dundie.database import connect
from pydantic import BaseModel, ValidationError, validator
from dundie.utils.email import check_valid_email


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise ValidationError("Email is Invalid")
        return v


class Balance(BaseModel):
    person: Person
    value: Union[Decimal, int, float]

    @validator("value", pre=True)
    def ensure_decimal(cls, v):
        return Decimal(v)

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Union[Decimal, int, float]

    @validator("value", pre=True)
    def ensure_decimal(cls, v):
        return Decimal(v)


db = connect()

people = []
for pk, data in db["people"].items():
    people.append(Person(pk=pk, **data))


person = people[0]
print(person.dict())

print(person.json())

balance = Balance(person=person, value=100)
print(balance.json(models_as_dict=False))
