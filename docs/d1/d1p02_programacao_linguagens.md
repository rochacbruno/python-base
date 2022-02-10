# Programação e Linguagens

## O computador e as linguagens

O computador, ou qualquer únidade computacional (um celular, um chip etc) é um
dispositivo eletrônico digital que por sua natureza só entende informações em
formato binário, o formato binário é um esquema lógico onde as informações são
formadas por sequencias de `0` e `1` encadeadas, cada um desses digitos é 
chamado de bit e a sequencia de 8 deles é chamada de Byte ex: `10010100` portanto
para enviar qualquer tipo de instrução ao computador precisamos colocar os bits
na ordem desejada e essa é uma tarefa humanamente bem dificil.

Por exemplo, toda vez que você pressiona a tecla `A` em seu teclado os componentes
do teclado precisam enviar a mensagem `10000001` para o computador que internamente
passa essa mensagem ao sistema operacional (windows, linux, mac, android etc) e
coverte essa sequencia em um número decimal, neste caso é o `65` e a partir
deste número o sistema operacional consegue ir até uma tabela de caracteres e 
consultar a letra que está presente na posição `65` que neste caso é o `A` e 
só então o `A` pode ser usado por exemplo para ser mostrado em sua tela.

Por isso que existem as linguagens de abstração para programação, todas as 
linguagens de programação tem por objetivo abstrair a necessidade de fazer esses
cálculos binários e trazer as intruções para uma camada mais próxima do ser humano
e mais longe da máquina.

Por isso classificamos as linguagens de programação entre as de "Baixo Nível" que 
são aquelas que diretamente convertem suas intruções para o código binário e 
muitas vezes tem uma sintaxe de escrita mais dificil e menos natural.

E as de "Alto Nível" que oferecem formas mais simples, em linguagem natural, com
palavras normais da lingua inglesa, porém entre o programa e o código binário
final existem uma série de camadas de abstração.

Python é uma linguagem de alto nível e vamos focar neste treinamento em suas
facilidades e abstrações.

## Programa

Um programa é um conjunto de intruções colocados de forma organizada em um ou
mais arquivos e que podem ser executados várias vezes obtendo os mesmos
resultados.

Existem 2 categorias de programas, os programas interpretados e os compilados.

Os compilados exigem que toda as linhas de código sejam avaliadas e validadas
antes do programa executavel ser gerado já na linguagem de máquina (0,1..) e
no momento da execução o programa está todo pronto para rodar.

Os programas interpretados são aqueles que podem ser escritos em arquivos mas
são avaliados linha a linha, bloco a bloco, sem a necessidade de o programa
inteiro estar avaliado, cada intrução é lida e logo em seguida interpretada e 
executada, este tipo de programação é mais fácil e mais dinâmica, mas pode ser 
também mais sucetivel a erros.

Python é uma linguagem dinâmica e interpretada e isso permite que a gente
envie comandos individuais, linha a linha para o interpretador e isso torna
a experiência de aprendizado bastante agradavél.
