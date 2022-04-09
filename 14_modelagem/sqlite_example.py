import sqlite3

con = sqlite3.connect("sqlite_example.db")
con.execute("PRAGMA foreign_keys = ON;")


instructions = """\
CREATE TABLE if not exists person (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    email varchar UNIQUE NOT NULL,
    dept varchar NOT NULL,
    role varchar NOT NULL
);
---
CREATE TABLE if not exists balance (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    value integer NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists movement (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer NOT NULL,
    value integer NOT NULL,
    date datetime NOT NULL,
    actor varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists user (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    password varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
"""

for instruction in instructions.split("---"):
    con.execute(instruction)


instruction = """\
INSERT INTO person (name, email, dept, role)
VALUES ('Karla', 'karla@rocha.com', 'Engineering', 'Programmer');
"""

con.execute(instruction)
con.commit()

instruction = """\
SELECT id, name, email, dept, role
FROM person ORDER BY name;
"""

cur = con.cursor()
result = cur.execute(instruction)
print(result)
for row in result:
    print(row)

instruction = """\
SELECT id, 100
FROM person ORDER BY name;
"""
cur = con.cursor()
result = cur.execute(instruction)  # sqlite3.Cursor

for row in result:  # Cursor implementa o protocolo Iterable
    instruction = "INSERT INTO balance (person, value) VALUES (?, ?)"
    con.execute(instruction, row)
con.commit()


instruction = """\
SELECT person.name, person.email, balance.value
from person
LEFT JOIN balance
WHERE person.id = balance.person
"""
cur = con.cursor()
result = cur.execute(instruction)
for row in result:
    print(row)
