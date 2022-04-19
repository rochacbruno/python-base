# https://www.ime.usp.br/~pf/dicios/br-utf8.txt
import unicodedata


def tira_acento(s):
    one = unicodedata.normalize("NFD", s)
    two = one.encode("ascii", "ignore")
    three = two.decode("utf-8")
    return three


original = open("br-utf8.txt").readlines()

with open("palavras.txt", "w") as palavras:
    palavras.write(
        "\n".join(
            [
                tira_acento(palavra.strip())
                for palavra in original
                if len(palavra.strip()) == 5
            ]
        )
    )
