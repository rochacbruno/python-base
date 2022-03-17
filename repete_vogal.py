"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

VOGAIS = "aeiouãõâôêéáíó"  # constante

words = []  # acumullator/acumulador
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word:  # condição de parada
        break

    final_word = ""  # acumullator/acumulador
    for letter in word:
        if letter.lower() in VOGAIS:
            final_word += letter * 2
        else:
            final_word += letter
        # final_word += letter * 2 if letter.lower() in VOGAIS else letter
    words.append(final_word)


print(*words, sep="\n")
