# Um ORM escrito com Pydantic

ORM significa Objetct Relational Mapping e é o nome dado a abordagem
de mapear dados serializados em bancos de dados relacionais com classes e objetos.

No projeto dundie implementamos um ORM baseado em classes Pydantic.

O objetivo é a utilização no formato:

```py
from dundie.database import connect, commit
from dundie.models import Person, Movement

db = connect()  # carrega os dados do arquivo JSON

pam = db[Person].get_by_pk("pam@dm.com")  # Busca Person através do e-mail
pam_movements = db[Movement].filter(person__pk=pam.pk)  # Filtro 

sales_persons = db[Person].filter(dept="Sales")
for person in sales_persons:  # iteração
    print(person.name)

pam.dept = "Management"  # update
commit(db)  # salva de volta no banco de dados
```

A implementação detalhada está em [https://github.com/rochacbruno/dundie-rewards/pull/22/files](https://github.com/rochacbruno/dundie-rewards/pull/22/files)


As principais alterações ocorreram nos arquivos:

- database.py
- models.py
- core.py

> Não foi necessário alterar nem o cli.py nem o esquema do banco dados.


Você pode obter localmente utilizando:

```bash
# Se já tiver um repositório com o projeto
git checkout -b orm
git pull https://github.com/rochacbruno/dundie-rewards

# Se quiser clonar em um projeto novo
git clone https://github.com/rochacbruno/dundie-rewards pasta_destino
cd pasta_destino
git fetch -all
git checkout pydantic_orm
```
