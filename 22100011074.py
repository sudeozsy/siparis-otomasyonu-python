""" NO: 22100011074                              -SİPARİŞ OTOMASYONU-
    AD-SOYAD: SUDE ÖZSOY"""

# musteri bilgileri dosyasındaki 6. sıra kullanıcı adı, 7. sıra şifredir.

musteri_bilgi = {}             # müşterilerin kullanıcı adı ve şifre bilgilerini tutar.
hesap = 0                      # siparişlerdeki toplam hesabı tutması için
top_must = 0                   # toplam müşteri sayısını hesaplamak için
giris = ""                     # menu2deki güncelle/sil/görüntüle seçenekleri için giriş yapılan idyi tutar.

with open("musteri_bilgileri.txt", "r", encoding="utf-8") as dosya:     # ilk olarak dosyadaki bilgileri okuması için
    veri = dosya.readlines()                   # müşteri bilgilerini satır satır listeye atar
    for i in veri:                             # her satırı ayrı ayrı gezmesi için
        bilgi = i.split("-")                   # dosyada - ile ayrılmış olan bilgileri alır yine listeye atar
        # bilgilerin 5 ve 6. indisinde her zaman id ve şifreler vardır. Listenin sonundaki \n'i silmek için -1 kullandım
        musteri_bilgi[bilgi[5]] = bilgi[6][0:-1]
        top_must += 1                          # top müşteri sayısını artırır.


def menu2():                                   # ana menü dışındaki 2. menü
    print("-"*40)
    secim = input("|1|-Sipariş Ekle\n|2|-Bilgilerimi Güncelle\n|3|-Bilgilerimi Görüntüle\n"
                  "|4|-Muşteri Kaydımı Sil\n|0|-Ana Menüye Dön\n   secin:")
    if secim == "1":
        siparisEkle()
    elif secim == "2":
        bilgiGuncelle()
    elif secim == "3":
        bilgilerimiAra()
    elif secim == "4":
        kayitSil()
    elif secim == "0":
        print("Çıkışınız yapılıyor...")
        return
    else:
        print("Yanlis sayi girisi!")
        menu2()


# ek fonks
def musteri_giris():                        # müşteri id ve şifre bilgisi ile 2. menüye aktarılır.
    global musteri_bilgi, top_must, giris
    print("-"*50)
    if top_must == 0:
        print("\U00002757Hiç kullanıcı bilgisi bulunamadı, önce kayıt olun!")
        return
    else:
        id = input("Kullanıcı Adı: ")
        parola = input("Parola: ")
        kontrol = 0
        for key, value in musteri_bilgi.items():    # tüm idleri gezer
            kontrol += 1                            # kaç kez gezdiğini hesaplar
            if key == id and value == parola:       # id ve şifre uyuşuyorsa 2. menüye yönlendirilir.
                print("\U0001F513Giriş yapıldı,hoşgeldiniz\U0001F642")
                giris = id
                menu2()
                return
            if top_must == kontrol:                 # tüm idler gezildiyse ve eşleşme olmadıysa yanlış giriş.
                print("\U00002757Yanlış şifre veya kullanıcı adı girişi!")
                return


# listeleme
def urunler():
    print("-----------ÜRÜNLER-----------")
    try:
        with open("urunler.txt", "r", encoding="utf-8") as dosya:    # txt'den tüm ürünleri çekip yazdırır.
            veri = dosya.readlines()
            kontrol = 0
            for i in veri:
                kontrol += 1
                if kontrol == 1 or kontrol == 2 or kontrol == 3:   # ürünlerin yanına emoji eklemek için kontrolle ayırdım.
                    print(i[0:-1]+"TL"+"\U0001F355")
                elif kontrol == 4 or kontrol == 5:
                    print(i[0:-1] + "TL" + "\U0001F354")
                elif kontrol == 6:
                    print(i[0:-1] + "TL" + "\U0001F9C6")
                elif kontrol == 7:
                    print(i[0:-1] + "TL" + "\U0001F35F")
                elif kontrol == 8:
                    print(i[0:-1] + "TL" + "\U0001F32F")
                elif kontrol == 9:
                    print(i[0:-1] + "TL" + "\U0001F35B")
                elif kontrol == 10:
                    print(i + "TL")
    except:
        urunler()


# arama
def musteriAra():
    global top_must
    print("-"*40)
    if top_must == 0:
        print("\U00002757Kayıtlı müşteri bulunmamaktadır, önce kayıt olun!")
    else:
        try:
            with open("musteri_bilgileri.txt", "r", encoding="utf-8") as dosya:
                ad_soyad = dosya.readlines()
                aranan = input("Aranacak müşteri ad-soyad bilgisini girin: ")
                kontrol = False
                for i in ad_soyad:
                    veri = i.split("-")
                    if veri[0].lower()+" "+veri[1].lower() == aranan.lower():  # aranan ve var olan isimleri küçük harfe çevirir.
                        kontrol = True         # eşleşme olduysa kontrol true olur
                        print("\U0001F4CDAranan müşterinin kaydı bulunmaktadır.")
                if kontrol == False:          # eşleme olmadığı durumda kontrol false kalır
                    print("\U0001F4CDAranan müşterinin kaydı bulunmamaktadır.")
        except:
            musteriAra()


# ekleme
def yeniMusteri():
    global top_must
    print("-"*40)
    print("Yeni müşteri bilgi girişi:")
    try:
        with open("musteri_bilgileri.txt", "a", encoding="utf-8") as dosya:
            dosya.write(input("Ad:") + "-")         # dosyaya her eklenen bilgi sonrası - koyulur
            dosya.write(input("Soyad:") + "-")
            dosya.write(input("Eposta:") + "-")
            dosya.write(input("Şehir:") + "-")
            dosya.write(input("Telefon:") + "-")
            while True:
                id = input("Kullanıcı Adı:")
                parola = input("Parola(En az 8 karakter):")
                if len(parola) >= 8:               # parolanın uzunlugu 8 karakterden fazla olması için
                    if len(musteri_bilgi) != 0:
                        for key, value in musteri_bilgi.items():
                            if id == key:         # kullanılan idlerden farklı bir id seçmesi için
                                print("\U000026A0Bu kullanıcı adı kullanılıyor.Tekrar deneyin.")
                                break
                            else:
                                musteri_bilgi[id] = parola      # id-şifre bilgisini sözlüğe de kaydeder
                                dosya.write(id + "-" + parola + "\n")    # dosyaya ekler
                                top_must += 1                   # toplam kullanıcı sayısını artırır.
                                print("\U0001F4CDMüşteri eklendi.\U0001F642")
                                return
                    else:
                        musteri_bilgi[id] = parola
                        dosya.write(id + "-" + parola + "\n")
                        top_must += 1
                        print("\U0001F4CDMüşteri eklendi.\U0001F642")
                        return
                else:
                    print("\U000026A0Parolanın en az 8 karakter olmasına dikkat edin!")
    except:
        yeniMusteri()


# ek fonks + iç içe fonks(kampanya ekle)
def siparisEkle():
    global hesap
    while True:
        urunler()       # urunler fonksiyonunu çağırıp ürünleri listeler
        print("(0) Önceki ekrana dön")
        with open("urunler.txt", "r", encoding="utf-8") as dosya:
            urun = dosya.readlines()
            secim = int(input("    Secim yapın-> "))
            if not 0 <= secim <= 10:         # 10 ürün olduğu için seçim 0-10 arası olmalı
                print("\U000026A0Yanlış sayi girişi!")
                siparisEkle()
            veri = urun[secim-1].split("-")

            fiyat = int(veri[1])             # verinin 1. indisi ürünlerin fiyatına denk geliyor
            adet = int(input("Kaç tane istiyorsunuz: "))
            fiyat *= adet                    # adet sayısıyla çarpıp fiyata ekler

        hesap += fiyat                       # toplam hesaba ekler.
        tekrar = input("Extra ürün eklemek için 1'i tuşlayın.Çıkış için herhangi bir şey tuşlayın:")
        if tekrar == "1":                    # tekrar ürün eklemesi için fonksiyonun başına gider.
            continue
        else:
            print(f"\U0001F4CDKampanyasız tutar: {int(hesap)}TL")
            kampanyaUygula()                 # ürün ekleme işlemi bitince kampanya ekleme fonksiyonuna gider
            return


# ek fonks
def kampanyaUygula():
    global hesap

    print("-"*10 + "KAMPANYALAR" + "-"*10)
    print("\U0001F3F7Sadece bir kapmanya secme hakkiniz vardir.\U0001F3F7")
    print("(1)-Ilk siparise 50Tl ustune 25Tl indirim!")
    print("(2)-Ogrenciye %15 indirim!")
    print("(3)-Carsamba gunlerine ozel %5 indirim!")
    print("Kampanyasız sipariş için herhangi bir tuşa basabilirsiniz.")
    print("-"*31)
    secim = input("->Secim yapın:")
    if secim == "1":
        dgr = input("->İlk siparişinizse 1'i tuşlayın:")
        if dgr == "1":                    # ilk siparişi olup olmadığını teyit etmesi için
            if hesap >= 50:               # hesap tutarının 50tlden fazlalığını teyit etmesi için
                hesap -= 25
                print(f"\U0001F4B5Ödemeniz gereken tutar-> {int(hesap)}")
                print("\U0001F4CDSiparişiniz alınmıştır, adresinize teslim edilecektir\U0001F642")
                hesap = 0                 # sipariş tamamnlandığında hesabı sıfırlar bi sonraki siparişler için
                menu2()
            else:
                print("\U000026A0Hesap tutari 50Tl'yi gecmis olmali!")
                kampanyaUygula()
        else:
            print("\U000026A0Bu kampanyadan yalnızca ilk siparişte yararlanılır.")
            kampanyaUygula()
    elif secim == "2":
        dgr = input("->Ogrenci iseniz 1'i tuşlayın:")
        if dgr == "1":
            hesap *= 85/100
            print(f"\U0001F4B5Ödemeniz gereken tutar-> {int(hesap)}")
            print("\U0001F4CDSiparişiniz alınmıştır, adresinize teslim edilecektir\U0001F642")
            hesap = 0
            menu2()
        else:
            print("\U000026A0Bu kampanyadan yalnızca öğrenciyseniz yararlanabilirsiniz.")
            kampanyaUygula()
    elif secim == "3":
        dgr = input("->Günlerden çarşamba 1'i tuşlayın:")
        if dgr == "1":
            hesap *= 95/100
            print(f"\U0001F4B5Ödemeniz gereken tutar-> {int(hesap)}")
            print("\U0001F4CDSiparişiniz alınmıştır, adresinize teslim edilecektir\U0001F642")
            hesap = 0
            menu2()
        else:
            print("\U000026A0Bu kampanyadan yalnızca günlerden çarşambaysa yararlanabilirsiniz.")
            kampanyaUygula()
    else:
        print(f"\U000026A0Kampanya kullanılmadı ve siparişiniz alındı.\n\U0001F4B5Ödemeniz gereken tutar->{int(hesap)}")
        hesap = 0
        menu2()


# guncelleme
def bilgiGuncelle():
    global giris
    with open("musteri_bilgileri.txt", "r", encoding="utf-8") as dosya:
        veri = dosya.readlines()
        satir = 0                             # dosyanın kaçıncı satırda olduğunu konrtol etmek için
        kontrol = False                       # kişiyi güncelleme durumunu kontrol eder güncellendiyse True olur
        parola = input("Şifreniz:")           # bilgilerini güncelleyebilmesi için id-şifre güvenliği koydum
        for i in veri:
            satir += 1                        # her satırda artar
            bilgi = i.split("-")
            if giris == bilgi[5] and parola == bilgi[6][0:-1]:    # id-şifre girilenle eşleşiyorsa
                if satir == 1:     # eğer dosyanın ilk satırında eşleşiyorsa öncelikle bilgileri siler sonra ekler.
                    with open("musteri_bilgileri.txt", "w", encoding="utf-8") as f:  # bu yüzden w ile açtım.
                        print("--Yeni bilgileri girin;")
                        f.write(input("Ad:") + "-")
                        f.write(input("Soyad:") + "-")
                        f.write(input("Eposta:") + "-")
                        f.write(input("Şehir:") + "-")
                        f.write(input("Telefon:") + "-")
                        while True:        # yeni id'nin kullanılmıyor oluşunu şifrenin 8'den uzun oluşunu kontrol eder.
                            cikis = 0
                            id_yeni = input("Kullanıcı adı:")
                            parola_yeni = input("Parola(En az 8 karakter):")
                            if len(parola_yeni) >= 8:
                                del (musteri_bilgi[giris])   # eski bilgileri siler aynı idsini kullanabilmesi için
                                kontrol = True
                                for key, value in musteri_bilgi.items():
                                    if id_yeni == key:
                                        print("Bu kullanıcı adı kullanılıyor.Tekrar deneyin")
                                        break
                                    else:   # şartlar sağlıyorsa kullanıcının yeni bilgilerini sözlüğe ve dosyaya ekler.
                                        f.write(id_yeni + "-" + parola_yeni + "\n")
                                        musteri_bilgi[id_yeni] = parola_yeni
                                        giris = id_yeni
                                        cikis = 1
                                        break
                                if cikis == 1:
                                    break
                            else:
                                print("Parolanın en az 8 karakter olmasına dikkat edin!")

                else:      # eğer dosyanın sonraki satırlarında eşleşiyorsa ilk bilginin ardına eklemeye devam eder.
                    with open("musteri_bilgileri.txt", "a", encoding="utf-8") as f:  # bu yüzden a ile açtım.
                        print("--Yeni bilgileri girin;")
                        f.write(input("Ad:") + "-")         # üsttekiyle aynı işlemler;
                        f.write(input("Soyad:") + "-")
                        f.write(input("Eposta:") + "-")
                        f.write(input("Şehir:") + "-")
                        f.write(input("Telefon:") + "-")
                        while True:
                            id_yeni = input("Kullanıcı adı:")
                            parola_yeni = input("Parola(En az 8 karakter):")
                            if len(parola_yeni) >= 8:
                                del (musteri_bilgi[giris])
                                kontrol = True
                                for key, value in musteri_bilgi.items():
                                    if id_yeni == key:
                                        print("Bu kullanıcı adı kullanılıyor.Tekrar deneyin")
                                        break
                                    else:
                                        f.write(id_yeni + "-" + parola_yeni + "\n")
                                        musteri_bilgi[id_yeni] = parola_yeni
                                        break
                            else:
                                print("Parolanın en az 8 karakter olmasına dikkat edin!")
                                continue
                            break
            else:                 # eğer güncellenecek kişi değilse de bilgileri olduğu gibi ekler.
                if satir == 1:  # ilk satırsa w ile açar
                    with open("musteri_bilgileri.txt", "w", encoding="utf-8") as f:
                        f.write(i)
                else:            # sonraki satırlar için a ile
                    with open("musteri_bilgileri.txt", "a", encoding="utf-8") as f:
                        f.write(i)
            if satir == len(veri) and kontrol == False:
                print("\U000026A0Yanlış kullanıcı adı veya şifre girişi!")
        menu2()


# arama
def bilgilerimiAra():
    global musteri_bilgi, giris
    kontrol = False
    parola = input("Şifreniz:")             # sadece kendi bilgilerine ulaşabilsin diye id-şifre güvenliği koydum.
    with open("musteri_bilgileri.txt", "r", encoding="utf-8") as dosya:
        veri = dosya.readlines()
        for i in veri:
            bilgi = i.split("-")
            if giris == bilgi[5] and parola == bilgi[6][0:-1]:
                kontrol = True            # eğer id-şifre uyuştuysa kontrol true olur ve bilgiler yazdırılır
                print(f"\U0001F7E3Ad: {bilgi[0]} \U0001F7E3Soyad: {bilgi[1]} \U0001F7E3Eposta: {bilgi[2]} "
                      f"\U0001F7E3Şehir: {bilgi[3]} \U0001F7E3Telefon: {bilgi[4]} \U0001F7E3Kullanıcı Adı: {bilgi[5]}")
                menu2()
        if kontrol == False:              # kontrol hiç true olmadıysa bilgiler yanlış girilmiş demektir
            print("\U000026A0Yanlış kullanıcı adı veya şifre girişi!")
            menu2()


# sil
def kayitSil():
    global giris
    with open("musteri_bilgileri.txt", "r", encoding="utf-8") as dosya:
        veri = dosya.readlines()
        satir = 0               # kaçıncı satırda olduğunu kontrol etmek için
        kontrol = False         # kişiyi silme durumunu kontrol eder silindiyse True olur
        cikis = 0
        parola = input("Şifreniz:")       # sadece kendi bilgilerini silebilsin diye id-şifre güvenliği koydum.
        for i in veri:
            satir += 1         # her satırda bir artar
            bilgi = i.split("-")
            if bilgi[5] != giris or bilgi[6][0:-1] != parola:  # giriş yapılan kuallanıcı dışındakileri eklemek için
                if satir == 1 or cikis == 1:   # ilk satırsa w ile açılır
                    with open("musteri_bilgileri.txt", "w", encoding="utf-8") as f:
                        cikis = 0
                        f.write(i)
                else:
                    with open("musteri_bilgileri.txt", "a", encoding="utf-8") as f:
                        f.write(i)
                if satir == len(veri) and kontrol == False:   # eğer tüm satırları gezip id-şifre eşleşmediyse tekrar doğru bilgi istenir
                    print("\U000026A0Yanlış kullanıcı adı veya şifre girişi!")
                    menu2()
            elif bilgi[5] == giris and bilgi[6][0:-1] == parola:
                # id-şifreyle eşleşen kişiyi dosyaya tekrar eklemez bu sayede silinmiş olur.
                print("Müşteri kaydınız silindi...\U0001F641Tekrar bekleriz.")
                del(musteri_bilgi[giris])
                cikis = 1
                kontrol = True


print("       HOŞGELDİNİZ\U0001F642")
while True:         # ilk menü burdan kontrol edilir. kullanıcı giriş yaptığında ikinci menü fonksiyonuna yönlendirilir.
    print("-"*30)
    secim = input("|1|-Muşteri Giriş\n|2|-Yeni Müşteri Ekle\n|3|-Ürünleri Listele\n"
                  "|4|-Müşteri Kaydı Sorgula\n|0|-Programı Kapat\n   seçin->")
    if secim == "1":
        musteri_giris()
    elif secim == "2":
        yeniMusteri()
    elif secim == "3":
        urunler()
    elif secim == "4":
        musteriAra()
    elif secim == "0":
        print("Güzel günler dileriz...Tekrar bekleriz\U0001F64B")
        exit()
    else:
        print("\U000026A0Yanlis sayi girisi!")
        continue
