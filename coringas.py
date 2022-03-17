# SOLID - Single REsponsibility
def funcao(*args, timeout=10, **options):
    for item in args:
        print(item)
    print(options)

    print(f"timeout {timeout}")


funcao(
    "Bruno",
    1,
    True,
    timeout=90,
    nome="Joao",
    cidade="Viana",
    data="hoje",
    banana=1,
    panela=3,
    teclado=True,
)
