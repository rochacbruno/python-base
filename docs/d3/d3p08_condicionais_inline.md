# Condicionais Inline


Condicionais em Python são escritas com a palavra `if` exemplo:


```py
aberto = True
if aberto:
    print("Boas vindas, pode entrar")
else:
    print("Desculpe, estamos fechados")
```

Essa mesma condicional pode ser expressa usando um condicional **ternário**
também chamado de **if inline**

```py
aberto = True
print("Boas vindas, pode entrar" if aberto else "Desculpe, estamos fechados")
```

Essa construção é bastante útil em casos onde precisamos atribuir variáveis:

```py
if temperatura > 30:
    mensagem = "Está calor"
else:
    mensagem = "Está frio"
```

Pode ser reescrito com:

```py
mensagem = "Está calor" if temperatura > 30 else "Está frio"
```

Operadores lógicos.

Também é possível usar operadores lógicos para criar condicionais abreviadas.

> **NOTA** Muito cuidado ao escolher esta opção, pois além de estar sujeita
> a falsos positivos também não é tão fácil de ler.

```py
aberto = True
print(aberto and "Boas vindas, pode entrar" or "Desculpe, estamos fechados")
```

O interessante é ver como os operadores lógicos `and` e `or` podem ser
usados para tomar decisões.