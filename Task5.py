class hedef_eded_tapma():
    def __init__(self ) :
        self.my_list = []
        
    def elave_et(self, ededler):
        for eded in ededler:
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
Eded.elave_et([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
Eded.listi_goster()
hedef = int(input("hedef eded daxil edin: "))
print("Hedefe Beraber Olan Ededlerin Indeksləri:", Eded.hedef_cemine_beraber_olan_ededlerin_indekslerini_tap(hedef))
    
