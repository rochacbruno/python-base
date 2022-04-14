import tkinter
from time import strftime

relogio = tkinter.Label()

relogio.pack()
relogio['font'] = "Helvetica 120 bold"
relogio['text'] = strftime("%H:%M:%S")


def tictac():
    agora = strftime("%H:%M:%S")
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(100, tictac)


tictac()
relogio.mainloop()
