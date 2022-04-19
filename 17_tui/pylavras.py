import os
import random
from rich.prompt import Prompt
from rich.console import Console


DIR = os.path.abspath(os.path.dirname(__file__))
emojis = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬜"}


def posicao_correta(letter):
    return f"[black on green]{letter}[/]"


def letra_correta(letter):
    return f"[black on yellow]{letter}[/]"


def incorreto(letter):
    return f"[black on white]{letter}[/]"


def computa_tentativa(guess, answer):
    acertos = []
    emojificado = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            acertos += posicao_correta(letter)
            emojificado.append(emojis["correct_place"])
        elif letter in answer:
            acertos += letra_correta(letter)
            emojificado.append(emojis["correct_letter"])
        else:
            acertos += incorreto(letter)
            emojificado.append(emojis["incorrect"])
    return "".join(acertos), "".join(emojificado)


MENSAGEM = (
    f"{posicao_correta('Boas vindas')} "
    f"{incorreto('ao')} "
    f"{letra_correta('Pylavras')}"
)
INSTRUCAO = "Adivinhe a palavra de 5 letras.\n"


def main():
    palavra_correta = random.choice(
        open(os.path.join(DIR, "palavras.txt")).readlines()
    ).strip().lower()
    tentativas = 6
    rodadas = 0

    console = Console()
    console.print(MENSAGEM)
    console.print(INSTRUCAO)

    emojificados = []
    acertados = []
    while rodadas < tentativas:
        tentativa = Prompt.ask("Digite 5 letras.").strip().lower()
        if len(tentativa) != 5:
            console.print("Please type [red]5 letters[/]")
            continue
        rodadas += 1
        acertos, emojificado = computa_tentativa(tentativa, palavra_correta)
        acertados.append(acertos)
        emojificados.append(emojificado)
        console.clear()
        console.print(MENSAGEM)
        for acertos in acertados:
            console.print(acertos)
        if tentativa == palavra_correta:
            break
    print(f"\nPYLAVRAS {rodadas}/{tentativas}\n")
    for em in emojificados:
        console.print(em)


if __name__ == "__main__":
    main()
