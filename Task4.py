class Şahmat():
    def __init__(self, rəng, xana):
        self.rəng = rəng
        self.xana = xana
    def hərəkət(self, yenixana):
      pass
class Piyada(Şahmat):
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if (self.rəng == "Ağ" and y1 == y + 1 and x1 == x) or \
                (self.rəng == "Ağ" and y == 1 and y1 == y + 2 and x1 == x) or \
                (self.rəng == "Qara" and y1 == y - 1 and x1 == x) or \
                (self.rəng == "Qara" and y == 6 and y1 == y - 2 and x1 == x):
            self.xana = yenixana
        else:
            print("Piyada belə hərəkət edə bilmir")
class At(Şahmat):
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if (abs(x1 - x) == 1 and abs(y1 - y) == 2) or \
                (abs(x1 - x) == 2 and abs(y1 - y) == 1):
            self.xana = yenixana
        else:
            print("At belə hərəkət edə bilmir")
class Qala(Şahmat):
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if x1 == x or y1 == y:
            self.xana = yenixana
        else:
            print("Qala belə hərəkət edə bilmir")
class Fil(Şahmat):
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if abs(x1 - x) == abs(y1 - y):
            self.xana = yenixana
        else:
            print("Fil belə hərəkət edə bilmir ")
class Vəzir(Şahmat):
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if x1 == x or y1 == y or abs(x1 - x) == abs(y1 - y):
            self.xana = yenixana
        else:
            print("Vəzir belə hərəkət edə bilmir")
class Şah(Şahmat):
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if abs(x1 - x) <= 1 and abs(y1 - y) <= 1:
            self.xana = yenixana
        else:
            print("Şah belə hərəkət edə bilmir")

piyada = Piyada("Ağ", (0, 1))
print(piyada)
piyada.hərəkət((0, 2))
print(piyada)
piyada = Piyada("Qara", (6,0))
print(piyada)
piyada.hərəkət((3,0))
qala = Qala("Qara", (0, 0))
print(qala)
qala.hərəkət((4, 0))
print(qala)
at = At("Ağ", (1, 0))
print(at)
at.hərəkət((2, 3))
print(at)
fil = Fil("Qara", (2, 0))
print(fil)
fil.hərəkət((5, 3))
print(fil)
vəzir = Vəzir("Qara", (3, 0))
print(vəzir)
vəzir.hərəkət((3, 3))
print(vəzir)
şah = Şah("Qara", (4, 0))
print(şah)
şah.hərəkət((4, 2))
print(şah)
