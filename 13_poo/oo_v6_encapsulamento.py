class Conta:
    _tipo_de_conta = "corrente"
    __id_interno = 985645

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    def depositar(self, value):
        self._saldo += value

    def sacar(self, value):
        self._saldo -= value
        return value

    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo")
        return self._saldo


conta = Conta(cliente="Bruno")
conta.depositar(100)
conta.sacar(10)
print(conta.consultar())
print(conta.cliente)
print(dir(conta))
