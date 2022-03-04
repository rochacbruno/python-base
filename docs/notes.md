--------------------------------------------------------------------------


- {k:v for .. enumerate("abcd")}
- decorator try function * times if fail
- https://www.cosmicpython.com/book/preface.html
- words english https://twitter.com/python_tip/status/1478126318969626634


---


## doctests

Python inclui um módulo chamado 

```py
def heron(a, b, c):
    """Calcula a area de um triangulo

    >>> heron(20, 20, 10)
    96.82458365518542
    >>> heron(30, 40, 28)
    419.4746714642018
    """
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5
```

```bash
python -m doctest doc_tests.py
```