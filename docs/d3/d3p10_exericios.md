# Exercicios

Agora vamos fazer uma série de exercícios de fixação.



## Faça um programa que imprime os números pares de 1 a 200

ex
`python numeros_pares.py`
```py

2
4
6
8
...
```

## Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar
sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temo vezes 3 for maior ou igual a umidade: "ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: Fr"🥶 Frio"io
temp <0: "ALERTA!!! ⛄ Frio Extremo."

ex:
```py
python3 temp.py 
temperatura: 30
umidade: 90
... 
"ALERTA!!! 🥵♒ Perigo de calor úmido"
```

## Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras
com suas vogais duplicadas.

ex:
```py
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
```

## Reserva hotel

Faça um programa de terminal que exibe ao usuário uma listas dos quartos disponiveis para
alugar e o preço de cada quarto, esta informação está disponível em um arquivo de texto
separado por virgulas.

`quartos.txt`
```
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
```

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
```
# cliente, quarto, dias
Bruno,3,12
```

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma 
mensagem informando que já está reservado.
