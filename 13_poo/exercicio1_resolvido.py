"""
Este programa pergunta ao usuário quais items ele deseja comprar
e calcula o valor total da compra.

1. Clique em Run e execute o programa para ver como ele funciona.
2. Para cada um dos comentários marcados abaixo efetue as alterações
   usando orientação a objetos.
"""
from decimal import Decimal


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = Decimal(valor)


produtos = {"1": Produto("Maça", 4.5), "2": Produto("Melancia", 6.3)}

print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")

# ("1", Produto(...))
for codigo, produto in produtos.items():
    print(f"{codigo} -> {produto.nome} - R$ {produto.valor:.2f}")



class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Compra:
    def __init__(self, cliente, items=None):
        self.cliente = cliente
        # if items is None:
        #     self.items = []
        self.items = items or []

    @property
    def total(self):
        """Calcula o total da compra"""
        total = sum(
            [item.produto.valor * item.quantidade for item in self.items]
        )
        return Decimal(total)

    def add_item(self, cod_produto, quantidade):
        self.items.append(Item(produtos[cod_produto], quantidade))


nome_cliente = input("Qual o seu nome?")
compra = Compra(nome_cliente)

while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break
    if cod_produto not in produtos:
        print("Codigo inválido tente novamente.")
        continue
    quantidade = int(input("Quantas Unidades?:").strip())
    compra.add_item(cod_produto, quantidade)

print(f"Olá, {compra.cliente}")
print(f"No seu carrinho de compras tem {len(compra.items)} item.")
print(f"O total da compra é {compra.total:.2f}")
