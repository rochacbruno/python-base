from tkinter import Tk, Label, Entry, Button, StringVar

# Criamos a janela principal
janela = Tk()

# Criamos os widgets
titulo = Label(janela, text="Seu Nome")
nome = Entry(janela)
var = StringVar()
mensagem = Label(janela, textvariable=var)


# Funções de callback
def function():
    nome_atual = nome.get()
    var.set(f"Olá, {nome_atual}")


# Botões de ação
diga_ola = Button(janela, text="Diga olá", command=function)
sair = Button(janela, text="Sair", command=janela.destroy)


# Posicionamos os elementos na janela
titulo.grid(column=1, row=1)
nome.grid(column=2, row=1)
mensagem.grid(column=1, row=2)
diga_ola.grid(column=2, row=3)
sair.grid(column=1, row=4)


# iniciamos o loop
janela.mainloop()
