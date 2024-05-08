class Şahmat():
    def __init__(self, rəng, xana):
        self.rəng = rəng
        self.xana = xana
        print("Şahmat yaradıldı")
    def hərəkət(self, yenixana):
        pass
class Top(Şahmat):
    def __init__(self, rəng, xana):
     super().__init__(rəng, xana)
    def hərəkət(self, yenixana):
        x, y = self.xana
        x1, y1 = yenixana
        if x1 == x or y1 == y:
            self.xana = yenixana
            print("Top üfüqi yaxud da şaquli hərəkət etdi")
        else:
            print("Top belə hərəkət edə bilmir")
top = Top("Qara", (0, 0))
top.hərəkət((4, 0))
top.hərəkət((0,1))
