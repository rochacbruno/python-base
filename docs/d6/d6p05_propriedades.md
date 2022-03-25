# Propriedades

A outras maneira de encapsular no Python é usando propriedades, é uma forma
bastante elegante e que utiliza um protocolo chamado `Descriptor`,
este modelo se parece bastante com o que vemos em outras linguagens de programação
como Java utilizando getters, setters e deleters.

```py
class Conta:
    _tipo_de_conta = "corrente"
    __id_interno = 985645

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    @property  # getter
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @saldo.deleter
    def saldo(self):
        self._saldo = 0


conta = Conta(cliente="Bruno")
conta.saldo = 100
conta.saldo = -10
print(conta.saldo)
```
```
90
```

```py
del conta.saldo
print(conta.saldo)
```
```
0
```

Uma grande vantagem em usar o padrão de properties é a possibilidade de
definir métodos internamente e expor como atributos sem a necessidade de 
parenteses para chamada.