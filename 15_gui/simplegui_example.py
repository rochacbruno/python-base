import PySimpleGUI as sg


def soma(x: int, y: int) -> int:
    return x + y


# https://pysimplegui.readthedocs.io/en/latest/#changlelookandfeel
sg.theme("Reddit")

layout = [
    [sg.Text("X"), sg.In(size=(5, 1), enable_events=True, key="x")],
    [sg.Text("Y"), sg.In(size=(5, 1), enable_events=True, key="y")],
    [sg.Text("", key="result")],
    [sg.Button("Calcula")],
    [],
    [sg.Button("Sair")],
]

window = sg.Window(title="Calcula", layout=layout, margins=(100, 50))


while True:
    event, values = window.read()
    if event == "Calcula":
        x = int(values["x"])
        y = int(values["y"])
        window["result"].update(soma(x, y))
    elif event in (sg.WIN_CLOSED, "Sair"):
        break


window.close()
