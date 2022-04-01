from instruments import Guitar, Flute, InstrumentKind, EletricGuitar, Distortion


gianini = Guitar("Giannini m2", kind=InstrumentKind.string, colors=["green"])
print(gianini)
print(gianini.play())
print("colors", gianini.colors)
print()

yamaha = Flute("Yamaha Magic Flute", colors=["silver"])
print(yamaha)
print(yamaha.play())
print("colors", yamaha.colors)
print()

lespaul = EletricGuitar("lespaul m1", colors=["brown", "yellow"])
print(lespaul)
print(lespaul.play(distortion=Distortion.normal))
print(lespaul.play(distortion=Distortion.whisper))
print(lespaul.play(distortion=Distortion.wave))
print("colors", lespaul.colors)
print()
