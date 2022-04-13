# Finalização do Projeto e Desafios


Chegamos so final do day7, calma, o curso ainda não acabou, ainda temos o day8
onde veremos demonstrações de vários tipos de projeto com Python.

Mas o projeto dundie nós finalizamos o MVP porém sobraram alguns desafios
para você resolver.


## Contribuindo com o Projeto Dundie

Essas instruções são para os alunos do treinamento Python Base
[https://www.linuxtips.io/products/python-base](https://www.linuxtips.io/products/python-base)

Você tem 4 issues para resolver e pode ve-las em: [https://github.com/rochacbruno/dundie-rewards/milestone/4](https://github.com/rochacbruno/dundie-rewards/milestone/4)

## Requisitos

- Escreva testes para as funcionalidades que adicionar
- Os testes precisam passar  no CI quando enviar o Pull Request

## Código de conduta

- Sem ofensas
- Ajude os colegas de treinamento

## Passo a passo para resolver os execicios

### Tenha um fork do repositório

- Clique em [https://github.com/rochacbruno/dundie-rewards/fork](https://github.com/rochacbruno/dundie-rewards/fork) e crie um fork (cópia) do repositório em sua conta do github

A partir de agora o repositório encontra-se em https://github.com/ SEU USER NAME / dundie-rewards

### Obtenha um clone do seu repositório

```bash
# se usar https
git clone https://github.com/seunome/dundie-rewards

# se tiver configurado o SSH
git clone git@github.com:seunome/dundie-rewards.git
```

### acesse a pasta e configure o `remote`

O remote `upstream` deve apontar para o repósitorio de `rochacbruno`

```bash
cd dundie-rewards
git remote add upstream https://github.com/rochacbruno/dundie-rewards
```

### Prepare o ambiente

```bash
make virtualenv
make install
make test
```

Neste ponto você já tem o projeto funcionando e já pode rodar

```bash
source .venv/bin/activate
dundie --help
```

no terminal para interagir com o programa.

### Implementação

Resolva as issues na ordem proposta em [https://github.com/rochacbruno/dundie-rewards/milestone/4](https://github.com/rochacbruno/dundie-rewards/milestone/4)

1. Crie uma branch para cada issue e.x:

```bash
git checkout -b issue_7
```

> Com o comando acima o git cria uma branch `issue_7` e você agora pode trabalhar no código

2. Abra o seu editor favorito e faça a implementação do código! boa sorte 🎉

3. Assegure-se da qualidade
   ```
   make fmt
   make lint
   make test
   ```
   - Os testes devem passar
   - Você deve adicionar novos testes para funcionalidades novas
   - A formatação do código tem que estar correta

4. Faça o commit ex:

```bash
git add .  # adiciona todos os arquivos alterados
git commit -m "Implementei a issue 7"
```
5. Faça o push

Para fazer um push você vai precisar de um access token do git e obter em

[https://github.com/settings/tokens](https://github.com/settings/tokens/new)
clique em "gerar access token", expiration "nunca",  dê um  nome "git" e marque todas as opções e clique em generate token.

Na próxima página copie seu token e salve em local seguro.

Mais ajuda em:
https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```bash
#configure seu cache de token
git config --global credential.helper cache
```

```
git push -u origin HEAD
Username:  seunome
Password: <cole aqui o token>
```

> Agora que fez o push a branch `issue_7` foi para seu repositório e você pode ir
a [https://github.com/rochacbruno/dundie-rewards](https://github.com/rochacbruno/dundie-rewards)
e clicar no botão "Novo Pull Request" e abrir o seu PR.

Ou se preferir na URL abaixo, substitua `seunome` pelo seu user do github.
```
https://github.com/rochacbruno/dundie-rewards/compare/main...seunome:issue_7?expand=1
```

> **atenção**: Não será feito merge do seu pull request, o objetivo é apenas rodar o CI e
> fazer os testes passarem, o seu PR ficará esperando aprovação para rodar os testes.

5. Volte a sua branch main e faça o rebase

```py
git checkout main
git rebase origin/issue_7
git log -n 1
```

> Agora você pode repetir o processo para implementar as outras issues.

6. Repita desde o item `1` para as outras issues, substituindo `issue_7` pela issue que estiver
implementando, ex: a próxima da lista é a `issue_4`

