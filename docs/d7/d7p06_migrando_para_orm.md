# Migrando nosso projeto para usar ORM SQLModel

> O código no inicio desta aula https://github.com/rochacbruno/dundie-rewards/tree/pydantic_orm


O SQLModel é uma extensão que junta o `Pydantic` ao `SQLALchemy` portanto
as classes que herdam de `SQLModel` são ao mesmo tempo BaseModel do Pydantic
e Table do SQLAlchemy.

## Modelagem

1. Começamos alterando o arquivo `models.py` e trocando a BaseModel do Pydantic
   pela base model `SQLModel` do  `sqlmodel` e setando `table` para true
   	```py
   	from sqlmodel import SQLModel, Field
   	Objeto(SQLModel, table=True)
	```
2. Trocamos os campos `pk` por uma definição de `id` condizente com chave primária
   em todas os models. (pk -> email em Person)
3. Trocamos os relacionamentos para usar um `Field` com foreign key
	`person_id: int = Field(foreign_key="person.id")`
4. Adicionamos as `Relationships`
	`person: Person = Relationship(back_populates="model_name")`
	e
	```
	balance: "Balance" = Relationship(back_populates="person")
	movement: "Movement" = Relationship(back_populates="person")
	user: "User" = Relationship(back_populates="person")
	```
5. Setamos os campos que são indices além das primary keys: `Field(index=True)`
6. Ajustamos os campos que armazenam valores decimais.
	```
	from pydantic import condecimal
	value: condecimal(decimal_places=3) = Field(default=0)
	```
7. Ajustamos o `datetime` para ser o proprio objeto sem o `isoformat`

## Db, Session e criação das tabelas

1. Alteramos o arquivo `database.py`
2. Importamos os models todos para o contexto do database
   `from . import models  # noqa` IMPORTANTE!!! os models precisam
   ser importados antes das tabelas serem criadas.
3. Apagamos todo o nosso ORM customizado :(
   Apagamos inclusive os métodos connect e commit pois agora o SQLModel irá
   cuidar disso.
   Movemos as funções `add_person`, `set_initial_password`
   `set_initial_balance` e `add_movement` para um arquivo chamado `utils/db.py`
   e já faremos os ajustes necessários.
4. No arquivo `database.py` criamos uma `engine` e uma função para obter uma
   `Session` e alteramos o `DATABASE_PATH` para um banco sqlite.
   E aproveirtamos para aplicar todo patch necessário.
   ```py
	from sqlmodel import Session, create_engine

	# We have to monkey patch this attributes
	# https://github.com/tiangolo/sqlmodel/issues/189
	from sqlmodel.sql.expression import Select, SelectOfScalar

	from dundie.settings import DATABASE_PATH

	from . import models

	SelectOfScalar.inherit_cache = True  # type: ignore
	Select.inherit_cache = True  # type: ignore

	engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)
	models.SQLModel.metadata.create_all(bind=engine)


	def get_session() -> Session:
	    with Session(engine) as session:
	        yield session

   ```
5. Ajustamos o utils.db
    - `db` agora é uma `session`
   - `ORM` não existe mais e agora basta importar os models, etc
   - table[model] não é mais necessário podemos usar queries diretamente
   - `pk` agora é `email`

   ```py

   ```
6. ajustamos os imports de utils.db em `core.py`

  ```py

  ```

7. Ajustamos o `cli.py`

```py
# cli:show
if len(result) == 0:
   click.echo("Nothing to show")
   return
```

8. Filtramos os warnings

```py
# database.py
import warnings
from sqlalchemy.exc import SAWarning

warnings.filterwarnings(
    'ignore', category=SAWarning
)
```


9. Ajustamos os tests unitarios

- conftest patch
