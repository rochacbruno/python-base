# Printable
# todos os objetos que implementam __str__
dados = [1, {"key": "value¨"}, True]
print(dados)


# customizando

class Cor:
    icon = "⬜"

    def __str__(self):
        return self.icon


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())


# Addible
# Todos os objetos que implementam __add__ e/ou __radd__


class ColorMixError(Exception):
    """Error when mising colors doesn't result"""


class Cor:
    def __str__(self):
        return self.icon

    def __eq__(self, other):
        return self.icon == other.icon

    def __add__(self, other):
        if not isinstance(other, Cor):
            raise ColorMixError("Unsuported types")
        if self == other:
            return self
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


print("Cores secundárias")
print(Amarelo() + Vermelho())
print(Azul() + Amarelo())
print(Vermelho() + Azul())
print(Amarelo() + Amarelo())

# print("Tipagem forte")
# print(Azul() + 1)


# Iterable
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])


print("rgb")
rgb = Paleta(Vermelho(), Verde(), Azul())
for cor in rgb:
    print(cor, end="")


# Container
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]


print("red in rgb?")
rgb = Paleta(Vermelho(), Verde(), Azul())
print("🟥" in rgb)


# Sized
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)


print("rgb size")
rgb = Paleta(Vermelho(), Verde(), Azul())
print(len(rgb))


# Sized + Container + Iterable = Collection

class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])

# Uma `Paleta` é uma `Collection` de `Cor`es.


# Subscriptable
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._cores[item]
        elif isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor

rgb = Paleta(Vermelho(), Verde(), Azul())
print(rgb[0])
print(rgb["azul"])


# Mais protocolos
# https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes


class Thing:
    ...


thing = Thing()
print(thing)  # __repr__ Representable
thing == 1  # __eq__ Equality Comparable
