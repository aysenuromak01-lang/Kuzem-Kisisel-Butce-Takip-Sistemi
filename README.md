# Kişisel Bütçe Takip Sistemi (Python Konsol Uygulaması)

Bu proje, Python programlama dilinin temel ve ileri seviye yapılarını (OOP, Hata Yönetimi, Veri Yapıları ve Dosya İşlemleri) kullanarak geliştirilmiş bir dönem sonu uygulama sınavı projesidir.

## Özellikler & Gereksinim Karşılamaları
- **OOP Mimari:** `Islem` (Varlık) ve `ButceYonetici` (Yönetici) adında 2 ana sınıf kullanılmıştır.
- **Kalıcı Veri:** Tüm kayıtlar program kapatılsa dahi silinmeyecek şekilde `butce_verileri.json` dosyasında saklanır.
- **Hata Yönetimi (try/except):** Dosya okuma (`JSONDecodeError`) ve kullanıcı sayısal veri girişlerinde (`ValueError`) çökmeleri önleyen yapılar kurulmuştur.
- **Gelişmiş Veri Yapıları:** Dinamik listeler, kategori bazlı dağılımlar için Python `sözlük (dict)` yapısı ve finansal özet aktarımları için `tuple` yapısı kullanılmıştır.
- **Raporlama:** Toplam gelir, gider, net kar durumu ve harcama kategorilerinin dağılımını gösteren detaylı bir özet ekranı sunulmaktadır.

## Nasıl Çalıştırılır?
Projeyi bilgisayarınıza klonladıktan sonra terminal veya komut satırından ana dosyayı çalıştırmanız yeterlidir:

```bash
git clone <REPORUZUN_LINKI>
cd <REPO_KLASORU>
python main.py
```
