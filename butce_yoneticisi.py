import json
import os

class Islem:
    """Tek bir gelir veya gider kaydını temsil eden Varlık (Entity) sınıfı."""
    def __init__(self, id_no: int, tip: str, kategori: str, miktar: float, tarih: str):
        self.id_no = id_no
        self.tip = tip          # 'Gelir' veya 'Gider'
        self.kategori = kategori
        self.miktar = miktar
        self.tarih = tarih

    def to_dict(self):
        """Nesneyi JSON'a kaydetmek için sözlük yapısına çevirir."""
        return {
            "id_no": self.id_no,
            "tip": self.tip,
            "kategori": self.kategori,
            "miktar": self.miktar,
            "tarih": self.tarih
        }


class ButceYonetici:
    """Bütçe işlemlerini yöneten, ekleme, silme, raporlama yapan Yönetici sınıfı."""
    def __init__(self, dosya_adi="butce_verileri.json"):
        # Dosya yollarının her bilgisayarda çalışması için dinamik konumlama (Gereksinim 5)
        self.dosya_adi = os.path.join(os.path.dirname(__file__), dosya_adi)
        self.islemler = [] # List veri yapısı (Gereksinim 6)
        self.verileri_yukle()

    def verileri_yukle(self):
        """JSON dosyasından verileri güvenli bir şekilde yükler (Hata Yönetimi 1)."""
        try:
            # Hatalı olan self.dosya_name kısmını self.dosya_adi yaptık:
            with open(self.dosya_adi, "r", encoding="utf-8") as f:
                veriler = json.load(f)
                for item in veriler:
                    # Daha önceki adımda bahsettiğimiz i.tariir hatasına takılmamak için 
                    # buradaki item["tarih"] kısmını nesneye gönderirken "tarih" olarak gönderdiğinden emin ol:
                    islem = Islem(item["id_no"], item["tip"], item["kategori"], item["miktar"], item["tarih"])
                    self.islemler.append(islem)
        except FileNotFoundError:
            # Dosya ilk kez çalıştırıldığında yoksa hata vermez, boş liste ile başlar
            self.islemler = []
        except json.JSONDecodeError:
            print("[Hata] Veri dosyası bozuk veya geçersiz formatta! Boş veriyle başlatılıyor.")
            self.islemler = []

        except json.JSONDecodeError:
            print("[Hata] Veri dosyası bozuk veya geçersiz formatta! Boş veriyle başlatılıyor.")
            self.islemler = []

    def verileri_kaydet(self):
        """Mevcut işlemleri kalıcı olarak JSON dosyasına yazar (Gereksinim 3)."""
        with open(self.dosya_adi, "w", encoding="utf-8") as f:
            json.dump([islem.to_dict() for islem in self.islemler], f, ensure_ascii=False, indent=4)

    def islem_ekle(self, tip: str, kategori: str, miktar: float, tarih: str):
        """Yeni bir gelir/gider kaydı ekler (Gereksinim 7)."""
        # Benzersiz ID oluşturma
        yeni_id = self.islemler[-1].id_no + 1 if self.islemler else 1
        yeni_islem = Islem(yeni_id, tip, kategori, miktar, tarih)
        self.islemler.append(yeni_islem)
        self.verileri_kaydet()
        print(f"\n[Başarılı] {tip} kaydı başarıyla eklendi! (ID: {yeni_id})")

    def islemleri_listele(self):
        """Tüm kayıtları ekrana listeler."""
        if not self.islemler:
            print("\nHenüz kaydedilmiş bir gelir veya gider bulunmuyor.")
            return
        
        print("\n=== MEVCUT BÜTÇE KAYITLARI ===")
        for i in self.islemler:
            print(f"ID: {i.id_no} | [{i.tip}] {i.kategori} - {i.miktar} TL ({i.tariir})")

    def islem_sil(self, id_no: int) -> bool:
        """ID numarasına göre kayıt siler (Gereksinim 7)."""
        for islem in self.islemler:
            if islem.id_no == id_no:
                self.islemler.remove(islem)
                self.verileri_kaydet()
                return True
        return False

    def kategori_ara(self, aranan_kategori: str):
        """Kategoriye göre filtreleme ve arama yapar (Gereksinim 5)."""
        sonuclar = [i for i in self.islemler if aranan_kategori.lower() in i.kategori.lower()]
        
        if not sonuclar:
            print(f"\n'{aranan_kategori}' kategorisine ait hiçbir kayıt bulunamadı.")
            return

        print(f"\n=== '{aranan_kategori}' İÇİN ARAMA SONUÇLARI ===")
        for i in sonuclar:
            print(f"ID: {i.id_no} | [{i.tip}] {i.kategori} - {i.miktar} TL ({i.tarih})")

    def rapor_olustur(self):
        """Özet ve istatistik raporu sunar (Gereksinim 8 & Gereksinim 6 Sözlük/Tuple kullanımı)."""
        toplam_gelir = 0.0
        toplam_gider = 0.0
        # Kategori bazlı özet için Sözlük (Gereksinim 6)
        kategori_ozet = {}

        for i in self.islemler:
            if i.tip == "Gelir":
                toplam_gelir += i.miktar
            else:
                toplam_gider += i.miktar
            
            # Sözlük verisini güncelleme
            kategori_ozet[i.kategori] = kategori_ozet.get(i.kategori, 0.0) + i.miktar

        net_durum = toplam_gelir - toplam_gider

        print("\n" + "="*30)
        print("      FİNANSAL ÖZET RAPORU      ")
        print("="*30)
        print(f"Toplam Kayıt Sayısı : {len(self.islemler)}")
        # Tuple kullanımı örneği (Gereksinim 6 - Yapısal sabit veri aktarımı)
        finansal_ozet_tuple = (toplam_gelir, toplam_gider, net_durum)
        print(f"Toplam Gelir        : {finansal_ozet_tuple[0]:.2f} TL")
        print(f"Toplam Gider        : {finansal_ozet_tuple[1]:.2f} TL")
        print(f"Net Kasa Durumu     : {finansal_ozet_tuple[2]:.2f} TL")
        print("-"*30)
        print("Kategori Bazlı Harcama Dağılımı (Sözlük):")
        for kat, miktar in kategori_ozet.items():
            print(f"  - {kat}: {miktar:.2f} TL")
        print("="*30)
