#!/usr/bin/env python3

original = [1, 2, 3]

# For loops / Laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}
dados = {}
for line in open("post.txt"):
    if ":" in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()

print(dados)
