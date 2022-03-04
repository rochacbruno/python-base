### Funções de primeira classe

Em Python funções também são objetos, e podem ser utilizadas como qualquer outro objeto, ou seja, uma função pode ser passada como paramêtro para outra função.


```python

# Digamos que tenhamos uma coleção de utilidades

def transforma_em_maiusculo(texto):
    return texto.upper()

def transforma_em_minusculo(texto):
    return texto.lower()

def divide_por_2(numero):
    return numero // 2

# e nossa função principal

def faz_algo(valor, funcao):
    return funcao(valor)

print(faz_algo("bruno", transforma_em_maiusculo))
# BRUNO

print(faz_algo("BRUNO", transforma_em_minusculo))
# bruno

print(faz_algo(10, divide_por_2))
# 5
```

E isso permite fazer uma enorme quantidade de composição de funções.

### Funções anonimas

As vezes é conveniente passar uma função como paramêtro para outra função, mas não queremos que essa função seja definida, pois será uma função de uso único.

```python
faz_algo(10, lambda x: x * 2)
# 20
faz_algo(10, lambda x: x // 2)
# 5
faz_algo("python é bom", lambda x: x.title())
# Python É Bom
```

A biblioteca padrão do Python utiliza deste recurso em uma grande parte de suas funções:

```python
nomes = ["Bruno", "João", "Maria", "Carlos", "Erik"]
print(sorted(nomes, key=len)
# ['João', 'Erik', 'Bruno', 'Maria', 'Carlos']

filter(lambda x: x.startswith("B"), nomes)
# ['Bruno']
```

Algumas regras:

- A função `lambda` pode receber argumentos
- A função `lambda` não pode retornar valor
- A função `lambda` não DEVE ser definida como variável
- A função `lambda` não pode ter mais de uma expressão

## Protocolo callable

As funções fazem parte dos objetos que implementam o protocolo `callable`, ao longo do treinamento veremos outros objetos `callable` e aprenderemos a adicionar este protocolo aos objetos.

Para verificar se um objeto é `callable` basta utilizar a função `callable`:

```python
print(callable(lambda x: x))
# True
```