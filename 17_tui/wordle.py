from rich.prompt import Prompt
from rich.console import Console

emojis = {"correct_place": "🟩", "correct_letter": "🟨", "incorrect": "⬜"}


def correct_place(letter):
    return f"[black on green]{letter}[/]"


def correct_letter(letter):
    return f"[black on yellow]{letter}[/]"


def incorrect(letter):
    return f"[black on white]{letter}[/]"


def score_guess(guess, answer):
    scored = []
    emojied = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            scored += correct_place(letter)
            emojied.append(emojis["correct_place"])
        elif letter in answer:
            scored += correct_letter(letter)
            emojied.append(emojis["correct_letter"])
        else:
            scored += incorrect(letter)
            emojied.append(emojis["incorrect"])
    return "".join(scored), "".join(emojied)


WELCOME_MESSAGE = (
    f"{correct_place('Welcome')} "
    f"{incorrect('to')} "
    f"{correct_letter('TERMINODLE')}"
)
P1_INSTRUCTIONS = "Player 1: Please enter a word (player 2, look away)\n"
P2_INSTRUCTIONS = "Player 2: You may start guessing\n"


def main():
    allowed_guesses = 6
    used_guesses = 0

    console = Console()
    console.print(WELCOME_MESSAGE)
    console.print(P1_INSTRUCTIONS)
    answer_word = Prompt.ask("Enter a word")
    console.clear()
    console.print(WELCOME_MESSAGE)
    console.print(P2_INSTRUCTIONS)

    all_emojied = []
    all_scored = []
    while used_guesses < allowed_guesses:
        guess = Prompt.ask("Enter your guess")
        if len(guess) != 5:
            console.print("Please type [red]5 letters[/]")
            continue
        used_guesses += 1
        scored, emojied = score_guess(guess, answer_word)
        all_scored.append(scored)
        all_emojied.append(emojied)
        console.clear()
        console.print(WELCOME_MESSAGE)
        for scored in all_scored:
            console.print(scored)
        if guess == answer_word:
            break
    print(f"\nTERMINODLE {used_guesses}/{allowed_guesses}\n")
    for em in all_emojied:
        console.print(em)


if __name__ == "__main__":
    main()
