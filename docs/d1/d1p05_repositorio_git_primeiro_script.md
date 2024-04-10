# Seu primeiro script

## Repositório

Antes de começar a programar seu primeiro script será necessário criar um
repositório no GitHub, neste local vamos armazenar e controlar o histórico
de alterações do programa.

Para criar o repositório, após fazer login no GitHub acesse https://github.com/new
basta preencher o nome com `python-base` e clicar em `create repository`.

O seu novo repositório estará acessível em:

https://github.com/USERNAME/python-base

> ***USERNAME** deve ser substituido pelo seu nome de usuário do GitHub.

### Configure seu GitHub

O primeiro passo é certificar que, localmente no seu computador ou no terminal
em que você está usando para o treinamento, você possui o git e ele esteja
configurado para seu usuário, basta digitar os comandos:

> Substitua "Seu Nome" pelo seu nome completo.

```bash
git config --global user.name "Seu Nome"
```

> Substitua "email@domain" pelo seu verdadeiro e-mail, o mesmo utilizado no GitHub.

```bash
git config --global user.email "email@domain"
```

Opcionalmente, você pode dizer ao git qual seu editor de código favorito.

> Substitua "Micro" pelo seu editor de escolha, ex: Vim, Nano, Code, Sublime...
 
```bash
git config --global core.editor "micro"
```

### Clone

Agora que seu git está configurado, vamos fazer o clone do seu repositório,
este processo vai criar uma cópia do repositório na sua máquina local.

Para fazer o clone existem alguns detalhes:

1. Escolha o caminho onde vai armazenar seu projeto, eu, por exemplo, coloco na
minha pastas de usuário em um subdiretório chamado `Projects` ex: `~/Projects`
acesse esta pasta antes de fazer o clone. Você pode escolher o local que preferir.

```bash
mkdir ~/Projects  # caso ainda não exista
cd ~/Projects
```

2. Agora você precisa escolher entre 2 modos de autenticação, o GitHub suporta
`https` e `ssh`, o `ssh` é o mais seguro e recomendado, mas exige que você tenha
suas chaves SSH configuradas, você pode ver como fazer isso aqui:
https://docs.github.com/pt/authentication/connecting-to-github-with-ssh

3. Efetue o clone.

Por `https` (não precisa de SSH, só tem que informar usuário e senha quando for alterar o repositório).

```bash
git clone https://github.com/USERNAME/python-base
```

por `SSH` (vantagem é não precisar informar usuário e senha quando alterarmos o repositório).
```bash
git clone git@github.com:USERNAME/python-base.git
```

Acesse seu repositório.

```bash
cd python-base
```

Durante o treinamento usaremos com frequência os seguintes comandos do git:

- `git status` para verificar o estado dos arquivos e se existem mudanças a aplicar
- `git add` para adicionar arquivos novos e adicionar mudanças em arquivos existentes
- `git commit` para confirmar uma alteração e marcar um __checkpoint__ no histórico do repositório
- `git push` para enviar as mudanças locais para o GitHub
- `git pull` para baixar mudanças do GitHub para o local
- `git commit -p` para o commit em modo interativo

## Seu Primeiro Script :) 

Obrigatoriamente, seu primeiro script deve ser um programa que imprime na tela 
a frase "Hello, World!"

Um script nada mais é do que o conjunto de comandos que enviamos individualmente
ao interpretador, mas de uma forma organizada em um único arquivo.

Da mesma forma que é possível executar:

```bash
python -c "print('Hello, World!')"
python -c "print(1 + 1)"
```

Você pode criar um arquivo e colocar os comandos em sequência, linha a linha 
dentro dele.

> Utilize o editor de sua preferência para criar um arquivo.

```bash
micro hello.py
``` 

Com o editor aberto, coloque o conteúdo do seu script.

```py=
print("Hello, World!")
```

Salve o script `ctrl + S` na maioria dos editores e em outro terminal execute

```bash
python3 hello.py
```
Ele retornará uma saída assim:

`Hello, World!`

> Repare que usamos `python3` para ser específico em relação à versão do Python 
utilizada para executar.
 
> Ao escrever uma nova parte do código é muito importante após efetuar os testes 
> fazer o `commit` para salvar o código.

```bash
# Exibe o status do repositório.
git status

# Adiciona o arquivo novo ou alterado no histórico do git.
git add nome_do_arquivo.py

# Efetua um commit marcando a alteração.
git commit -m "Criado meu primeiro hello world"

# Envia as mudanças para o GitHub.
git push   # Sua senha pode ser pedida aqui caso tenha usado https.
```

## Comentários no código

Em Python é possível adicionar partes do código que serão ignoradas pelo
interpretador, essas linhas são úteis para adicionar comentários, lembretes e
metadados do programa.

Exemplos

```py
# Comentário de linha

print("Hello")  # Comentário de final de linha

"""
comentário 
multi
linhas
"""
```

As linhas iniciadas em `#` são ignoradas pelo Python
assim como tudo que estiver após `#` em uma linha de código
e também todo o conteúdo dentro de `"""`


## Shebang

Em ambientes Linux é muito importante definir o comentário especial
Shebang, nele especificamos qual interpretador será usado para
executar o programa:

```py=
#!/usr/bin/env python3

print("Hello, World!")
```

A primeira linha informa o terminal que aquele programa roda com o Python 3 da `env`
em execução, esta forma é possível omitir o interpretador e executar o script
diretamente pelo seu nome.

```bash
# Primeiro damos permissão de execução ao script.
chmod +x hello.py
```

Agora podemos executar de 2 formas:

```bash
# Especificando o interpretador na linha de comando.
python3 hello.py
```

```bash
# Usando o interpretador especificado na linha `#!/usr/bin/env python`
./hello.py
```

A vantagem da segunda forma é que podemos mudar a extensão de `.py` para `.exe`,
por exemplo, ou podemos até remover a extensão e executar `./hello`
