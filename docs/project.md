# Projeto Dundie Rewards

Nós fomos contratados pela Dunder Mifflin, grande fabricante de papéis para desenvolver um sistema
de recompensas para seus colaboradores.

Michael, o gerente da empresa quer aumentar a motivação dos funcionários oferecendo um sistema
de pontos que os funcionários podem acumular de acordo com as suas metas atingidas, bonus oferecidos
pelo gerente e os funcionários podem também trocam pontos entre sí.

O funcionário pode uma vez a cada ano resgatar seus pontos em um cartão de crédito para gastar onde
quiserem.

Acordamos em contrato que o MVP (Minimum Viable Product) será uma versão para ser executada no terminal
e que no futuro terá também as interfaces UI, web e API.

Os dados dos funcionários atuais serão fornecidos em um arquivo que pode ser no formato .csv ou .json
e este mesmo arquivo poderá ser usado para versões futuras. `Nome, Depto, Cargo, Email`

MVP - Terminal 0.1.0

User Stories:

Epic: Administração

- EU como ADMIN quero ser capaz de EXECUTAR O COMANDO `dundie load people.txt` para alimentar o banco de dados com as informações dos funcionários.
    - Para cada funcionario no arquivo caso ainda não exista no banco de dados deverá ser criado com a pontuação inicial de `100` para gerentes e `500` para associados, caso já exista as informações diferentes deverão ser atualizadas e
    a pontuação somada.
    - O sistema deve evitar entrada de associados em duplicidade, e aceitar apenas e-mails válidos.
    - O sistema deve criar uma senha inicial para cada funcionário e enviar por email.
    - Os dados deverão ser armazenados em um banco de dados SQL.

- EU como ADMIN quero ser capaz de VISUALIZAR no terminal um relatório contendo as informações dos funcionários
    -  No terminal desejo ver Nome, e-mail, saldo de pontos, data da última atualização
    - Este relatório deverá ter a opção de ser salvo em um arquivo .txt
    - `dundie show --dept|--email|--output`

- Eu como ADMIN quero ser capaz de atribuir pontos para um funcionário especifico ou para todo um departamento.
    - `dundie add --dept|--email --value=100`
    - `dundie remove --dept|--email --value=100`

- Eu como ADMIN quero que as operações de ADMIN sejam protegidas por usuário e senha.

Epic: Movimentação

- Eu como FUNCIONARIO quero ser capaz de visualizar meu saldo de pontos e extrato de movimentações.
- Eu como FUNCIONARIO quero ser capaz de transferir pontos para outro funcionário
- Eu como FUNCIONARIO quero que as operações sejam protegidas por senha, impedindo que outro usuário altere minha conta
