#!/user/bin/env python
"""Imprime a mensagem de um e-mail

NAO MANDE SPAM!!!
"""
__version__ = "0.1.0"


email_tmpl = """
Olá, %(nome)s
 
Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s
 
Clique agora em %(link)s
 
Apenas %(quantidade)d disponiveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
