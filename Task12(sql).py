import sqlite3
connection = sqlite3.connect("Library")
cursor = connection.cursor()
def create_table():#burada 3 cedvel yaratdim(kitablar, abonentler ve borca goturulen kitablar)
 cursor.execute("CREATE TABLE IF NOT EXISTS KİTABLAR (kitab_id INTEGER PRIMARY KEY AUTOINCREMENT,başlıq TEXT NOT NULL,müəllif TEXT NOT NULL,nəşr_ili INTEGER,janr TEXT, dil TEXT CHECK( dil IN ('ingilis', 'azerbaycan')) NOT NULL)")
 cursor.execute("CREATE TABLE IF NOT EXISTS ABONENTLƏR (abonent_id INTEGER PRIMARY KEY AUTOINCREMENT,ad TEXT NOT NULL,soyad TEXT NOT NULL,email TEXT)")
 cursor.execute("CREATE TABLE IF NOT EXISTS ÖDÜNÇ (kitab_id INTEGER NOT NULL, abonent_id INTEGER NOT NULL,ödünç_alma_tarixi DATE NOT NULL, qaytarma_tarixi DATE NOT NULL, FOREIGN KEY (kitab_id) REFERENCES KİTABLAR (kitab_id), FOREIGN KEY (abonent_id) REFERENCES ABONENTLƏR (abonent_id))")
 connection.commit()
create_table()#cedvelleri ise saldim
def add_kitab():#kitablar cedveline kitablari dinamik elave etmek ucun funksiya yaratdim
    başlıq = input("Kitabın adı: ")
    müəllif = input("Kitabın müəllifi: ")
    nəşr_ili = int(input("Nəşr ili: "))
    janr= input("Janr: ")
    while True:
        dil = input("Kitabın dilini seçin (ingilis/azerbaycan): ").lower()
        if dil in ('ingilis', 'azerbaycan'):
            break
        else:
            print("Xəta: Yalnız 'ingilis' və ya 'azerbaycan' seçə bilərsiniz.")
    cursor.execute("INSERT INTO KİTABLAR (başlıq, müəllif, nəşr_ili, janr, dil) VALUES (?, ?, ?, ?, ?)", (başlıq, müəllif, nəşr_ili, janr, dil))
    connection.commit()
print("Kitab əlavə edildi")
def add_abonent():#burada abonentleri dinamik elave etmek ucun funskiya yaratdim
    ad = input("Abonentin adı: ")
    soyad = input("Abonentin soyadı: ")
    email= input("Email: ")
    cursor.execute("INSERT INTO ABONENTlƏR (ad, soyad, email) VALUES (?, ?, ?)", (ad, soyad, email ))
    connection.commit()
    print("Abonent əlavə edildi")
def add_borc_kitab():#burada odunc goturulen kitablari dinamik elave etmek ucun funksiya yaratdim
    kitab_id = int(input("Kitab ID: "))
    abonent_id = int(input("Abonent ID: "))
    ödünç_alma_tarixi = input("Ödünç alma tarixi (YYYY-MM-DD): ")
    qaytarma_tarixi = input("Qaytarma tarixi (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO ÖDÜNÇ (kitab_id, abonent_id, ödünç_alma_tarixi, qaytarma_tarixi) VALUES (?, ?, ?, ?)", (kitab_id, abonent_id, ödünç_alma_tarixi, qaytarma_tarixi))
    connection.commit()
    print("Borc götürülən kitab əlavə edildi")
def qaytar_kitab(): #burada qaytarilan kitabi dinamiki silmek ucun funksiya yaratdim
    kitab_id = int(input("Qaytarılan kitabın ID'si: "))
    abonent_id = int(input("Abonentin ID'si: "))
    cursor.execute("DELETE FROM ÖDÜNÇ WHERE kitab_id = ? AND abonent_id = ?", (kitab_id, abonent_id))
    connection.commit()
    print("Qaytarılan kitab borc kitablar siyahısından silindi")
def abonenti_sil():#burada kitablari qaytarmis abonenti dinamiki silmek ucun funksiya yaratdim
    abonent_id = int(input("Silinəcək abonentin ID'si: "))
    cursor.execute("DELETE FROM ÖDÜNÇ WHERE abonent_id = ?", (abonent_id,))
    cursor.execute("DELETE FROM ABONENTLƏR WHERE abonent_id = ?", (abonent_id,))
    connection.commit()
    print("Abonent və borcları silindi")
def sorted_to():#nesr iline gore cesidleme
    cursor.execute("SELECT * FROM KİTABLAR WHERE nəşr_ili<2000")
    print("XXI əsrdən əvvəlki kitablar: ", cursor.fetchall())
    cursor.execute("SELECT * FROM KİTABLAR WHERE nəşr_ili>2000")
    print("Bu əsrin kitabları: ", cursor.fetchall())
def add_dropdwn():#burada kitabxanaciya secim verdim hansi funksiyaani cagirmaq isteyir deye
    while True:
        print("/n1. Yeni kitab əlavə edin: ")
        print("2.Yeni abonent əlavə edin: ")
        print("3.Yeni ödünç kitab əlavə edin: ")
        print("4.Qaytarilan kitabi silin: ")
        print("5.Abonenti silin: ")
        print("6.Kitabları nəşr ilinə görə çeşidləyin: ")
        print("7. Çıxış")
        seçim = input("Seçiminizi edin: ")
        if seçim == "1":
            add_kitab()
        if seçim == "2":
            add_abonent()
        if seçim == "3":
            add_borc_kitab()
        if seçim == "4":
            qaytar_kitab()
        if seçim == "5":
            abonenti_sil()
        if seçim == "6":
            sorted_to()
        if seçim == "7":
            break
        else:
            print("Yanlış seçim. Seçiminizi düzgün daxil edin: ")
add_dropdwn()
connection.close()