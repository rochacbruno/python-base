"""
Este programa pergunta ao usuário quais items ele deseja comprar
e calcula o valor total da compra.

1. Clique em Run e execute o programa para ver como ele funciona.
2. Para cada um dos comentários marcados abaixo efetue as alterações
   usando orientação a objetos.
"""
from decimal import Decimal
from dataclasses import dataclass, field
from rich.table import Table
from rich.console import Console


console = Console()


@dataclass
class Produto:
    nome: str
    _valor: Decimal

    @property
    def valor(self) -> Decimal:
        return self._valor

    @valor.setter
    def valor(self, value: Decimal | int):
        self._valor = Decimal(value)


produtos = {
    "1": Produto("Maça", Decimal(4.5)),
    "2": Produto("Melancia", Decimal(6.3)),
}


print("Olá cliente, boas vindas à quitanda!")
table = Table(title="Produtos disponíveis")
table.add_column("Código")
table.add_column("Produto")
table.add_column("Valor")
for codigo, produto in produtos.items():
    table.add_row(str(codigo), produto.nome, f"{produto.valor:.2f}")
console.print(table)


@dataclass
class Item:
    produto: Produto
    quantidade: int


@dataclass
class Cliente:
    nome: str

    def __str__(self) -> str:
        return self.nome


@dataclass
class Compra:
    cliente: Cliente
    items: list[Item] = field(default_factory=list)

    @property
    def total(self) -> Decimal:
        """Calcula o total da compra"""
        total = sum(
            [item.produto.valor * item.quantidade for item in self.items]
        )
        return Decimal(total)

    def __len__(self):
        return len(self.items)

    def __iadd__(self, other):
        cod_produto, quantidade = other
        self.items.append(Item(produtos[cod_produto], quantidade))
        return self

    def __str__(self) -> str:
        return f"No carrinho tem {len(self)} item e custa R${self.total:.2f}"

    def show(self):
        table = Table(title=f"Carrinho de compras de {self.cliente}")
        table.add_column("nome")
        table.add_column("valor")
        table.add_column("quantidade")
        for item in self.items:
            table.add_row(
                item.produto.nome,
                f"{item.produto.valor:.2f}",
                str(item.quantidade)
            )
        table.add_row()
        table.add_row("[bold magenta]Total[/]", "", f"{self.total:.2f}")
        console.print(table)


nome_cliente = input("Qual o seu nome?")
cliente = Cliente(nome_cliente)
compra = Compra(cliente)


while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break
    if cod_produto not in produtos:
        print("Codigo inválido tente novamente.")
        continue
    quantidade = int(input("Quantas Unidades?:").strip())
    compra += (cod_produto, quantidade)


compra.show()
