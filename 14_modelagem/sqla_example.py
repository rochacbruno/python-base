from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

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
    person = relationship("Person", foreign_keys="Balance.person_id")


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
