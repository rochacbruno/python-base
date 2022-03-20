def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâôêéáíó":
            breakpoint()
            final_word = letter * 2  # HINT
        else:
            final_word = letter  # hint
    return final_word


print(repete_vogal("banana"))
