"""Tkinter"""

from typing import Tuple, Callable
from tkinter import Tk, Frame, Button, Entry, Label, StringVar


def soma(x: int, y: int) -> int:
    return x + y


def cria_janela_principal() -> Tuple[Tk, Frame]:
    janela = Tk()
    frame = Frame(janela)
    frame.grid()
    return janela, frame


def cria_entry(frame: Frame, text: str) -> Entry:
    label = Label(frame, text=text)
    label.grid()
    entry = Entry(frame)
    entry.grid()
    return entry


def cria_label_vazio(frame: Frame) -> StringVar:
    variable = StringVar()
    label = Label(frame, textvariable=variable)
    label.grid()
    return variable


def cria_botao(frame: Frame, text: str, command: Callable) -> Button:
    button = Button(frame, text=text, command=command)
    button.grid()
    return button


def main():
    janela, frame = cria_janela_principal()
    entry_x = cria_entry(frame, "X")
    entry_y = cria_entry(frame, "Y")
    result = cria_label_vazio(frame)
    cria_botao(
        frame,
        "Calcula",
        lambda: result.set(soma(int(entry_x.get()), int(entry_y.get()))),
    )
    cria_botao(frame, "sair", janela.destroy)
    janela.mainloop()


if __name__ == "__main__":
    main()
