def yerleri_tap():
    istirakçı_sayı = int(input("İstirakçı sayısını daxil edin: "))
    xallar = []
    yerler = []
    for i in range(istirakçı_sayı):
        xal = int(input(f"{i+1}-ci istirakçının xalını daxil edin: "))
        xallar.append(xal) 
    for xal in sorted(xallar, reverse=True):
        yer = str(xallar.index(xal)+1) + "-ci istirakci"
        yerler.append(yer)
    return yerler
yerler = yerleri_tap()
print(yerler)
