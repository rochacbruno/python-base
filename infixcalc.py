#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
infixcalc.py sum 5 2
7

infixcalc.py mul 10 5
50

infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("Digite a operação:").strip()
    n1 = input("n1:")
    n2 = input("n1:")
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("Ex uso: `sum 5 5`")
    sys.exit(1)
else:
    operation, n1, n2 = arguments

# TODO: Tratar Exception ValueError
for num in (n1, n2):
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido `{num}`")
        sys.exit(1)

if operation not in ("sum", "sub", "mul", "div"):
    print("Operação Inválida, escolha entre:")
    print(operations)
    sys.exit(1)

# TODO: Escolher entre int e float
n1 = float(n1)
n2 = float(n2)

# TODO: Trocar por dict de functions
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result:.1f}")








