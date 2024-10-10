def bilgi_alma():
    ad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı Giriniz: ")
    
    while True:
        try:
            yas = float(input("Yaşınızı Giriniz: "))
            if yas <= 0:
                print("Lütfen geçerli bir yaş giriniz.")
            else:
                break
        except ValueError:
            print("Lütfen sayısal bir değer giriniz.")

    okul = input("Liseden Mezun Olduğunuz Okul: ")

    while True:
        try:
            puan = float(input("YKS Yerleştirme Puanınızı Yazınız: "))
            if puan < 0 or puan > 500:
                print("Lütfen 0-500 arasında geçerli bir puan giriniz.")
            else:
                break
        except ValueError:
            print("Lütfen sayısal bir değer giriniz.")
    
    return ad, soyad, yas, okul, puan

def iban_dogrulama(hak):
    while hak > 0:
        iban = input("Lütfen İban Numaranızı Giriniz: ")
        
        if not iban.isdigit():
            print("Yalnızca sayı girmelisiniz!")
        elif len(iban) != 6:
            print("IBAN numarası tam 6 haneli olmalıdır!")
        else:
            print("IBAN hesabınıza tanımlanmıştır:", iban)
            return True
        
        hak -= 1
        print(f"Hatalı deneme, kalan hak: {hak}")
    
    print("Deneme hakkınızı doldurdunuz! Lütfen bir süre bekleyiniz.")
    return False

def ek_bilgiler_alma():
    while True:
        telno = input("Lütfen Telefon Numaranızı Giriniz (10 haneli): ")
        if len(telno) == 10 and telno.isdigit():
            break
        else:
            print("Geçersiz telefon numarası. 10 haneli rakam giriniz.")
    
    anne = input("Anne adınız: ")
    baba = input("Baba adınız: ")
    adres = input("Yaşadığınız il/ilçe? (İl/İlçe şeklinde yazınız): ")
    
    return telno, anne, baba, adres

def bilgi_kontrol(ad, soyad, yas, okul, puan, telno, anne, baba, adres):
    print("\nBilgileriniz:\n"
          "Adınız: " + ad + "\n"
          "Soyadınız: " + soyad + "\n"
          "Yaşınız: " + str(yas) + "\n"
          "Liseden Mezun Olduğunuz Okul: " + okul + "\n"
          "YKS Puanınız: " + str(puan) + "\n"
          "Telefon Numaranız: " + telno + "\n"
          "Anne Adı: " + anne + "\n"
          "Baba Adı: " + baba + "\n"
          "Adresiniz: " + adres)

ad, soyad, yas, okul, puan = bilgi_alma()

if puan >= 500:
    print("Sayın", ad, soyad, ", Geçersiz Puan Girdiniz!")
elif puan <= 300:
    print("Üzgünüz!", ad, soyad, "Farklı bir bölüm seçmeyi deneyin!")
else:
    print("Sayın", ad, soyad, "Tebrikler, bu bölüme seçildiniz!")

if iban_dogrulama(3):
    print("TEBRİKLER! İkinci aşamaya geldik. Şimdi lütfen istenilen bilgileri doldurunuz.")
    telno, anne, baba, adres = ek_bilgiler_alma()

    islem = input("İşleme devam etmek istiyor musunuz? (E/H): ").upper()

    if islem == "E":
        secenek = input("Yapmak istediğiniz işlemin numarasını yazın!\n1. Bilgi Kontrol\n2. İşlemi Sonlandır\n")
        
        if secenek == "1":
            bilgi_kontrol(ad, soyad, yas, okul, puan, telno, anne, baba, adres)
        elif secenek == "2":
            print("Hoşçakalın...")
        else:
            print("Geçersiz seçenek.")
    else:
        print("İşlem iptal edildi.")
else:
    print("İban doğrulaması başarısız olduğu için işlem sonlandırıldı.")
