from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Iterator, Tuple


@dataclass
class Produto:
    nome: str
    _valor: Decimal

    @property
    def valor(self) -> Decimal:
        return self._valor

    @valor.setter
    def valor(self, value: Decimal | int | float):
        self._valor = Decimal(value)


@dataclass
class Estoque:
    _items: List[Produto] = field(default_factory=list)

    def add_produto(self, produto: Produto):
        self._items.append(produto)

    def listar(self) -> List[Produto]:
        return self._items

    def __iter__(self) -> Iterator[Tuple[str, Produto]]:
        return iter(
            [
                (str(cod_produto), produto)
                for cod_produto, produto in enumerate(self._items, 1)
            ]
        )

    def pegar_produto_pelo_codigo(self, cod) -> Produto:
        return self._items[int(cod) - 1]

    def __getitem__(self, item) -> Produto:
        return self.pegar_produto_pelo_codigo(item)



estoque = Estoque()
estoque.add_produto(Produto("Maça", Decimal(4.5)))
estoque.add_produto(Produto("Melancia", Decimal(6.3)))

print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")
for codigo, produto in estoque:
    print(f"{codigo} -> {produto.nome} - R$ {produto.valor:.2f}")


@dataclass
class Item:
    produto: Produto
    quantidade: int


@dataclass
class Cliente:
    nome: str

    def __str__(self):
        return self.nome


@dataclass
class Compra:
    cliente: Cliente
    items: List[Item] = field(default_factory=list)

    @property
    def total(self) -> Decimal:
        """Calcula o total da compra"""
        total = sum(
            [item.produto.valor * item.quantidade for item in self.items]
        )
        return Decimal(total)

    def add_item(self, produto: Produto, quantidade: int):
        self.items.append(Item(produto, quantidade))


nome_cliente = input("Qual o seu nome?")
cliente = Cliente(nome_cliente)
compra = Compra(cliente)


while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break

    produto = estoque.pegar_produto_pelo_codigo(cod_produto)
    # produto = estoque[cod_produto]

    quantidade = int(input("Quantas Unidades?:").strip())
    compra.add_item(produto, quantidade)

print(f"Olá, {compra.cliente}")
print(f"No seu carrinho de compras tem {len(compra.items)} item.")
print(f"O total da compra é {compra.total:.2f}")
