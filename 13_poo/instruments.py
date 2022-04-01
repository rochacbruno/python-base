# Abstração e Herança com dataclasse?
# Tem enum no Python?
# dataclasses com valor default dão erro.
# para que serve o super()?

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List


# Enumeração / Enumerador
class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"
    normal = "normal"


class ABCInstrument(ABC):

    @abstractmethod
    def play(self):
        ...


@dataclass
class DataInstrumentMixin:
    name: str
    sound: str
    kind: InstrumentKind
    colors: List[str] = field(default_factory=list)

    def __str__(self):
        return f"<Instrument name:{self.name} kind:{self.kind.value}>"

class Instrument(DataInstrumentMixin, ABCInstrument):
    ...


@dataclass
class Guitar(Instrument):
    n_strings: int = 6
    sound: str = "Ding Ding Ding"
    kind: InstrumentKind = InstrumentKind.string
    colors: List[str] = field(default_factory=lambda: ["red", "black"])

    def play(self):
        return self.sound


@dataclass
class EletricGuitar(Guitar):
    sound: str = "Wah Wah Wah"

    def play(self, distortion: Distortion = Distortion.wave):
        return_from_base_class = super().play()
        if distortion is Distortion.wave:
            return "~~~".join(return_from_base_class.split())
        elif distortion is Distortion.whisper:
            return "...".join(return_from_base_class.split())
        return return_from_base_class



@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind
    colors: List[str] = field(default_factory=lambda: ["beige", "white"])

    def play(self):
        return self.sound
