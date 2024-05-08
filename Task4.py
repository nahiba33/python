class Şahmat():
    def __init__(self, rəng, xana):
        self.rəng = rəng
        self.xana = xana
        print("Şahmat yaradıldı")
    def hərəkət(self, yenixana):
        pass
class Qala(Şahmat):
    def __init__(self, rəng, xana):
     super().__init__(rəng, xana)
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if x1 == x or y1 == y:
            self.xana = yenixana
            print("Qala üfüqi yaxud da şaquli hərəkət etdi")
        else:
            print("Qala belə hərəkət edə bilmir")
qala = Qala("Qara", (0, 0))
qala.hərəkət((4, 0))
qala.hərəkət((0,1))
