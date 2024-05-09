class hedef_eded_tapma():
    def __init__(self ) :
        self.my_list = []
        
    def elave_et(self, eded):
        self.my_list.append(eded)
    def listi_goster(self):
        print(self.my_list)
    def hedef_cemine_beraber_olan_ededlerin_indekslerini_tap(self, hedef):
        indeksler = []
        for i in range(len(self.my_list)):
            for j in range(i+1, len(self.my_list)):
                if self.my_list[i] + self.my_list[j] == hedef:
                 indeksler.append((i, j))
        if not indeksler:
         return -1
        return indeksler

Eded = hedef_eded_tapma()
Eded.elave_et(1)
Eded.elave_et(2)
Eded.elave_et(3)
Eded.elave_et(4)
Eded.elave_et(5)
Eded.elave_et(6)
Eded.elave_et(7)
Eded.listi_goster()
hedef = 7
print("Cemi:", hedef)
print("Hedefe Beraber Olan Ededlerin Indeksləri:", Eded.hedef_cemine_beraber_olan_ededlerin_indekslerini_tap(hedef))
    
