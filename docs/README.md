# Python Expert

Um resumo dos treinamentos  contidos no Python Expert.

1. **BASE** - Conceitos fundamentais que formam a base para iniciar com Python,
   neste treinamento além de toda a base fundamental teórica tem muito execício prático
   e a criação de um  projeto de backend em terminal completo com interfaces, banco de dados
   e testes.

2. WEB - Python focado no desenvolvimento de backend para web e APIs usando os
   principais frameworks do mercado como Django, Flask e FastAPI, neste treinamento
   criaremos um mesmo projeto cobrindo as principais necessidades do mercado web e usando
   os 3 principais frameworks.

3. Automação - Python com foco em automação de operações em ambientes
   DevOps, Ci, Cloud, Testes, Qualidade de Software, neste treinamento falaremos sobre
   sockets, subprocessos, code coverage, comunicação com cloud providers e módulos Ansible, análise de performance e criação de wrapers para APIs.

4. Engineer - Para quem quer ir além da base, neste módulo vamos
   explorar conceitos avançados de Python, async, metaprogramação, descritores,
   criaremos nosso próprio framework e falaremos sobre inspeção de objetos e hooks.


## Python BASE

Você está iniciando o Python BASE que é o primeiro passo para começar
a sua carreira em desenvolvimento, este treinamento é pensado para
pessoas que nunca tiveram contato com programação antes, ou que já
possuem algum conhecimento em alguma outra linguagem e precisam aprender
Python e vamos desde a teoria base do que é programação, instalação e configuração do ambiente,
escolha de um editor de código e criação do seu primeiro script até
a criação de vários pequenos programas que vão abordar as principais
funcionalidades do Python e vamos também criar um projeto completo do zero com as
melhores práticas do mercado.

Duração estimada em horas: 64h

---
## Conteudo:

## Day 1 - Iniciando no mundo da programação

Neste capítulo você terá uma introdução ao treinamento e aos conceitos básicos de programação
e a linguagem Python, também aprenderá como instalar e preparar um ambiente para programar.

01. Introdução
00. Programação e Linguagens
00. Como é organizada a plataforma Python
00. Instalação e preparação do ambiente
00. Repositório, git e seu primeiro script
00. Variáveis de ambiente
00. Tipos de instruções
00. Organização de blocos de código
00. Ambientes virtuais, instalação de pacotes e Ipython

Duração: 5h

## Day 2 - Tipos e estruturas de dados

Neste capítulo você conhecerá os tipos e estruturas de dados do Python e execicios
práticos para entender como manipulamos informações.

10. Protocolos e Tipos de dados primitivos
00. Float, Bool, None
00. Textos, Caracteres e Strings
00. Formatação de texto
00. Tipos de dados compostos e Tuplas
00. Listas
00. Exercicio com Listas, Tuplas, Loops e Condicionais
00. Sets (conjuntos)
00. Dicionários
00. Exercicio: Refatorando nosso Hello World com dicionários

Duração: 7h

## Day 3 - Input, Output, Processamento

Nesta parte do treinamento o foco é obter informações do usuário, aplicar algortimo para
processar e persistir a informação em arquivos.

20. Stdin e Stdout
00. Leitura de inputs do stdin e de argumentos do terminal
00. Exercicio de criação de uma calculadora infix com input e argumentos
00. Filesystem - Manipulação de arquivos e pastas
00. Exercicio - Criando um bloco de anotações no terminal
00. Tratamento de Erros LBYL e EAFP
00. Logging - Formatando e gravando logs
00. Algoritmos e lógica - Condicionais, Operadores compostos
00. Condicionais ternárias e inline
00. Repetições com for, while e comprehensions.
00. Exercicio: Sistema de Reservas com iterators, textos, inputs e arquivos de texto.

Duração: 10h

## Day 4 - Funções, Debugging e seu primeiro projeto.

Neste capítulo terá muito conteúdo sobre funções com exercicios práticos e em seguida
aprenderá técnicas e ferramentas para depurar erros do programa e em seguida aprenderá
a criar seu próprio projeto com as melhores práticas.

31. Funções builtin uteis - sum, len, vars, min, max, filter, map
00. Funções úteis da biblioteca padrão - random, pprint, itertools, functools, smtplib etc
00. Definindo suas próprias Funções e aplicando fórmula matemática
00. Anatomia detalhada de funções - assinatura, argumentos, retornos
00. Escopos e namespaces e argumentos coringas
00. Funções lambda
00. Exercicio com lambda, recursão e introdução a programação funcional
00. Debugging - Técnicas e ferramentas para encontrar erros.
00. O Sistema de imports do Python
00. Criando um repositótio para seu primeiro projeto e configurando o VSCode
00. Estrutura de pastas, build e install do projeto
00. Entry points com console scripts
00. Gestão de dependencias e Makefile

Duração: 12h

## Day 5 - Qualidade de Software e de Código

Nesta parte focamos em testes, integração continua e qualidade do projeto incluindo
testes unitários, testes de integração e adequação com code style além de uma introdução
a documentação de software e empacotamento.

44. Introdução a testes + Doctest, Pytest e Decorators
00. Diferençá entre unit e integration tests, configuração do Pytest e CI com Github Actions
00. Boas práticas em testes e test reports
00. Qualidade de código, linters e auto formatação
00. Escolhendo boas ferramentas e libraries
00. Introdução ao TDD
00. Introdução a persistencia de dados e testes
00. Documentação de projetos, Empacotamento e Distribuição no PyPI

Duração: 10h

## Day 6 - Orientação a Objetos

Uma das principais caracteristicas da linguagem Python é a aplicação da Orientação a Objetos
seguindo um modelo que é um pouco diferente do tradicional e muito flexivel, neste capítulo
falaremos sobre toda a base da orientação a objetos com Python.

52. Os paradigmas de programação
00. Introdução a Orientação a Objetos
00. Inicialização de instâncias
00. Os 4 pilares da O.O: Abstração, Herança, Polimorfismo, Encapsulamento
00. Encapsulamento com properties
00. Python Data Model e Protocolos
00. Python Moderno, Type Annotations e Dataclasses
00. Dataclass abstrata, Enums, field e super()
00. Structural Pattern Matching

Duração: 7h

## Day 7 - Consumindo e armazenando dados.

Na maior parte dos programas sempre teremos que carregar e armazenar dados e para isso
precisamos aprender a usar bancos de dados SQL e consultar APIs.

61. Modelangem de dados com dataclasses e Pydantic
00. Prova de conceito de um ORM
00. Introdução a SQL e SQLite
00. SQL Alchemy
00. SQL Model
00. Convertendo software legado para SQL
00. Database Migrations e Consumindo API Rest
00. Finalização do Projeto e desafios

Duração: 8h

## Day 8 - Demonstrações

Nesta última parte do treinamento a intenção é fazer uma demonstração bastante breve a
respeito das ferramentas e frameworks principais do mercado, o formato não será de aula
mas sim de mão na massa, seguindo o mesmo projeto desenvolvido no treinamento vamos
adicionar interfaces Gráfica (GUI), 2D (Pygame), terminal (TUI), web (html) e API (REST).

69. Interface Gráfica para Desktop - Demonstração com Tk e Pysimplegui
00. Interface 2D para games - Demonstração com Pygame
00. Interface Gráfica para Terminal - Demonstração com Textual (game)
00. Interface web com html - Demonstração com Flask
00. Interface API com REST/Json - Demonstração com FastAPI

Duração: 5h
