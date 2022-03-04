nome = "Global"


def funcao():
    nome = "Local"
    print("Nome Local:", nome)
    nome = globals()["nome"]
    print("Nome Global:", nome)


funcao()
