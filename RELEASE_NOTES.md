# Otonom WhatsApp v1.1.0 Sürüm Notları

**Tarih:** 8 Mart 2024

## 🎉 Yeni Sürüm Özellikleri

Bu sürüm, kullanıcı deneyimini önemli ölçüde iyileştiren ve uygulamanın daha güvenilir çalışmasını sağlayan birçok yeni özellik ve iyileştirme içermektedir.

### ✨ Yeni Özellikler

- **Medya Mesajları**: Artık her medya dosyası için özel mesaj tanımlayabilirsiniz
- **Yıldız İşareti**: Mesaj eklenen medya dosyaları yıldız işareti (⭐) ile işaretlenir
- **Otomatik Ayarlar**: Delay ve wait değerleri otomatik olarak kaydedilir
- **Gelişmiş Numara Kontrolü**: Geçersiz numaralar daha hızlı ve doğru tespit edilir

### 🔧 İyileştirmeler

- **Ayrı Mesaj Gönderimi**: Medya dosyaları ve ana mesaj artık ayrı ayrı gönderiliyor
- **Dayanıklı Arayüz**: WhatsApp Web arayüz değişikliklerine karşı daha dayanıklı
- **Gizlilik**: Numaralar artık settings.json dosyasına kaydedilmiyor
- **Performans**: Gereksiz bekleme süreleri optimize edildi

### 🐛 Hata Düzeltmeleri

- **Medya Mesaj Karışması**: Medya mesajları ve ana mesajın karışması sorunu çözüldü
- **Input Elementi**: Medya yükleme sonrası input elementi değişikliği sorunu çözüldü
- **Bekleme Süreleri**: Gereksiz bekleme süreleri optimize edildi

## 📋 Kurulum

1. Python 3.8 veya üstü sürümü yükleyin
2. Gerekli kütüphaneleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
3. Uygulamayı başlatın:
   ```
   python main2.py
   ```

## ⚠️ Önemli Notlar

- Bu sürüm, WhatsApp Web'in en son sürümüyle uyumlu olacak şekilde test edilmiştir
- Numaralar artık settings.json dosyasına kaydedilmediği için, uygulamayı her başlattığınızda numaraları yeniden eklemeniz gerekecektir
- Medya mesajları ve ayarlar (delay, wait) hala kaydedilmektedir

## 🔄 Önceki Sürümden Güncelleme

v1.0.0 sürümünden güncelleme yapıyorsanız, settings.json dosyanız otomatik olarak yeni formata dönüştürülecektir. Numaralar artık kaydedilmeyeceği için, numaralarınızı yeniden eklemeniz gerekecektir.

## 🙏 Teşekkürler

Bu sürümü geliştirmemize yardımcı olan tüm kullanıcılarımıza teşekkür ederiz. Geri bildirimleriniz ve önerileriniz, uygulamanın daha iyi hale gelmesine yardımcı oluyor.

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın. 