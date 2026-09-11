from butce_yoneticisi import ButceYonetici

def ana_menu():
    yonetici = ButceYonetici()

    while True:
        print("\n*** KİŞİSEL BÜTÇE TAKİP SİSTEMİ ***")
        print("1. Gelir/Gider Ekle")
        print("2. Tüm İşlemleri Listele")
        print("3. İşlem Sil")
        print("4. Kategoriye Göre Ara/Filtrele")
        print("5. Özet Rapor Görüntüle")
        print("6. Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-6): ").strip()

        if secim == "1":
            print("\n--- Yeni Kayıt Ekleme ---")
            tip_secim = input("İşlem Tipi (1: Gelir, 2: Gider): ").strip()
            tip = "Gelir" if tip_secim == "1" else "Gider"
            
            kategori = input("Kategori (örn. Maaş, Market, Fatura): ").strip()
            if not kategori:
                print("[Hata] Kategori alanı boş bırakılamaz!")
                continue

            # Geçersiz sayısal giriş senaryosu (Hata Yönetimi 2)
            try:
                miktar = float(input("Miktar (TL): "))
                if miktar <= 0:
                    print("[Hata] Miktar sıfırdan büyük olmalıdır!")
                    continue
            except ValueError:
                print("[Hata] Lütfen miktar alanına geçerli bir sayı giriniz!")
                continue

            tarih = input("Tarih (GG.AA.YYYY - Boş bırakılırsa bugün): ").strip()
            if not tarih:
                from datetime import datetime
                tarih = datetime.now().strftime("%d.%m.%Y")

            yonetici.islem_ekle(tip, kategori, miktar, tarih)

        elif secim == "2":
            yonetici.islemleri_listele()

        elif secim == "3":
            yonetici.islemleri_listele()
            try:
                silinecek_id = int(input("\nSilmek istediğiniz işlemin ID numarasını girin: "))
                if yonetici.islem_sil(silinecek_id):
                    print(f"[Başarılı] ID: {silinecek_id} olan kayıt silindi.")
                else:
                    print("[Hata] Bu ID numarasına sahip bir kayıt bulunamadı!")
            except ValueError:
                print("[Hata] ID numarası bir tam sayı olmalıdır!")

        elif secim == "4":
            aranan = input("\nAramak istediğiniz kategori adını girin: ").strip()
            if aranan:
                yonetici.kategori_ara(aranan)
            else:
                print("[Uyarı] Arama yapabilmek için bir kelime yazmalısınız.")

        elif secim == "5":
            yonetici.rapor_olustur()

        elif secim == "6":
            print("\nProgramdan çıkılıyor. İyi günler!")
            break
        else:
            print("\n[Hata] Geçersiz bir seçim yaptınız. Lütfen 1-6 arasında bir rakam girin.")

if __name__ == "__main__":
    ana_menu()
