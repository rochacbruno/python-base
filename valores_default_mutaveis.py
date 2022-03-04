# set, dict, list


def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista


adiciona_a_lista(4)
adiciona_a_lista(4)
adiciona_a_lista(4)
adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))
