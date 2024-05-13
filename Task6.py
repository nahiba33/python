class Bank():
    def __init__(self, hesab_no, balans):
        self.hesab_no = hesab_no
        self.balans = balans
    
    def balans_artırmaq(self, məbləğ):
        self.balans += məbləğ
        print(f"{məbləğ} AZN balansınıza daxil oldu. Cari balans:{self.balans}")
         
    def balans_çıxarmaq(self, məbləğ):
        if self.balans >= məbləğ:
            self.balans -= məbləğ
            print(f"{məbləğ} AZN balansınızdan çıxarıldı. Cari balans {self.balans}")
        else :
            print("Hesabınızda kifayət qədər vəsait yoxdur.")
            
    def balans_göstərmək(self):
        print(f"Balans: {self.balans}") 
        
class Kredit(Bank):
    def __init__(self, hesab_no, balans, kredit_məbləği):
        super().__init__(hesab_no, balans)
        self.kredit_məbləği = kredit_məbləği

    def kredit_vermək(self):
      aylıq_ödəniş = self.kredit_məbləği / 12
      print(f"Aylıq ödəniş: {aylıq_ödəniş} AZN")
      self.balans_artırmaq(self.kredit_məbləği)

    def kredit_ödəmək(self, ödəniləcək_məbləg):
        if ödəniləcək_məbləg <= self.kredit_məbləği:
            self.kredit_məbləği -= ödəniləcək_məbləg
            self.balans -= ödəniləcək_məbləg
            print(f"{ödəniləcək_məbləg} AZN kredit ödənilmişdir. Qalan kredit: {self.kredit_məbləği} AZN. Balans:{self.balans}")
        else:
            print("Kredit məbləği balansınızdan çoxdur. Ödəniş etmək mümkün deyil.")

def hesab_nömrəsi():
    while True:
        hesab_no = input("Zəhmət olmasa hesab nömrənizi daxil edin: ")
        if hesab_no.isdigit() and len(hesab_no) == 16:
            return hesab_no
        else:
            print("Hesab nömrəsi 16 simvoldan ibarət olmalıdır.")

hesab_no = hesab_nömrəsi()
balans = int(input("Balansı daxil edin: "))
bank_hesabı = Bank(hesab_no, balans)
bank_hesabı.balans_göstərmək()
art_məbləğ = int(input("Balansı artırmaq üçün məbləği daxil edin: "))
bank_hesabı.balans_artırmaq(art_məbləğ)
azl_məbləğ = int(input("Çəkmək istədiyiniz məbləği daxil edin: "))
bank_hesabı.balans_çıxarmaq(azl_məbləğ)

kredit_məbləği = int(input("Kredit məbləğini daxil edin: "))
kredit_hesabı = Kredit(hesab_no, balans, kredit_məbləği)
kredit_hesabı.kredit_vermək()
ödəniləcək_məbləğ = int(input("Ödəniləcək kredit məbləğini daxil edin: "))
kredit_hesabı.kredit_ödəmək(ödəniləcək_məbləğ)
kredit_hesabı.balans_göstərmək()
