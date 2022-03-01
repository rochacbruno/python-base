# Algoritmos

Sequencia de instruções lógicas que visam obter a solução de 
um problema.

Problema: Ir a padaria e comprar pão:
Premissa: Padaria da Esquina abre fds: até 12h, semana até 19h, feriado (exceto Natal) não abre.

1. A padaria está aberta?
    1. Se é feriado e NÃO é natal: não
    2. Senão, Se é sábado OU domingo E antes do meio dia:  sim
    3. Senão, se é dia de semana E antes das 19h: sim
    4. senão: não
2. Se padaria está aberta E:
    1. Se está chovendo: Pegar guarda-chuvas
    2. Se está chovendo E calor: Pegar guarda-chuvas e garrafa de agua
    3. Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
    4. Ir até a padaria:
        1. Se tem pao integral E baguete: Pedir 6 de cada
        2. Senão, se tem apenas pao integral OU baguete: Pedir 12
        3. Senão: Pedir 6 de qualquer pão
3. Senão
    1. Ficar em casa em comer bolachas

## Statements

- Se -> If (condicao)
- Senão -> elif (condicao) / else

## Operadores lógicos

- E -> and (condicao composta com porta lógica AND)
- OU -> or (condicao composta com porta lógica OR)
- NÃO -> not (sinal de negação)

## Assignments

- A padaria está aberta? (boll, True|False)

## Expressions

- É feriado e NÃO é natal
- é sábado OU domingo E antes do meio dia?
- é dia de semana E antes das 19h?
- ...

## Ações

- pegar
- ir
- pedir
- tem
- comer


## Transformando em código


```py

import pegar, ir, pedir, tem, comer

# Premissas
today = "Segunda"
hora_atual = 15
natal = False
chovendo = True
frio = False
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriados = ["Quarta"]
horario_padaria {
    "semana": 19,
    "fds": 12,
}

# Algoritmo

# A padaria está aberta?
if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora_atual < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora_atual < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda chuva")
    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir(6, "pao integral")
        pedir(6 "baguete")
    elif tem("pao integral") or tem("baguete"):
        pedir(12, "pao integral ou baguete")
    else:
        pedir(6, "qualquer pao")
else:
    comer("bolachas")
```