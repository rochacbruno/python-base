from dataclasses import dataclass


@dataclass
class Pessoa:
    pk: str
    name: str
    points: int = 100


def funcao(dados: Pessoa):
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

print(dados.name)

funcao(dados)
