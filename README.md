# Otonom WhatsApp Toplu Mesaj Gönderme Uygulaması

Bu uygulama, WhatsApp Web üzerinden toplu mesaj göndermenizi sağlayan bir araçtır. Medya dosyaları ve özel mesajlar ekleyerek kişiselleştirilmiş mesajlar gönderebilirsiniz.


![Ana Ekran](https://github.com/yunusemretom/whatsapp-bulk-messenger/blob/primary/imgs/video.gif)

# Nasıl Kullanılır?

- Uygulamanın cihazınıza uygun sürümünü release kısmından indirin.
- Numaraları ülke kodları ile birlikte(90, 03, 68 vb.) metin dosyasına(txt) ekleyin. Her numaradan sonra bir satır atlayarak ekleyin.
- Uygulamayı çalıştırın. Uygulamayı imzalayamadığımız için büyük ihtimalle size çalıştırma tarzında bir uyarı çıkabilir. Bu uyarı "yine de çalıştır" deyip atlayabilirsiniz.
- Son olarak metinlerinizi girin ve arkanıza yaslanın. 
- *Dikkat edin eğer aynı numaradan birden fazla varsa aynı numaraya aynı mesaj birden fazla gidebilir.*


## 📦 Sürüm Bilgisi

**v1.1.0** (2024-03-08)

### Değişiklikler

- ✨ **Yeni Özellikler**
  - Her medya için özel mesaj tanımlama
  - Medya mesajlarını yıldız işareti ile görüntüleme
  - Ayarları otomatik kaydetme (delay, wait değerleri)
  - Geçersiz numara kontrolü iyileştirildi

- 🔧 **İyileştirmeler**
  - Medya dosyaları ve ana mesaj ayrı ayrı gönderiliyor
  - WhatsApp Web arayüz değişikliklerine karşı daha dayanıklı
  - Daha hızlı geçersiz numara tespiti
  - Numaralar artık settings.json dosyasına kaydedilmiyor

- 🐛 **Hata Düzeltmeleri**
  - Medya mesajları ve ana mesajın karışması sorunu çözüldü
  - Medya yükleme sonrası input elementi değişikliği sorunu çözüldü
  - Gereksiz bekleme süreleri optimize edildi

## ⚠️ Sorumluluk Reddi

Bu uygulama, WhatsApp'ın resmi bir uygulaması değildir ve WhatsApp tarafından desteklenmemektedir. Uygulamanın kullanımından doğabilecek her türlü sonuç kullanıcının sorumluluğundadır. Spam gönderimi, izinsiz mesaj gönderimi veya WhatsApp'ın kullanım şartlarına aykırı herhangi bir faaliyet için uygulama kullanılmamalıdır. Uygulamayı kullanarak, tüm yasal ve etik sorumlulukları kabul etmiş olursunuz.

## Özellikler

- 📱 Toplu WhatsApp mesajı gönderme
- 📎 Medya dosyaları (resim, video, PDF) ekleme
- 💬 Her medya için özel mesaj tanımlama
- ⭐ Medya mesajlarını yıldız işareti ile görüntüleme
- ⚙️ Ayarları otomatik kaydetme
- 🔄 Geçersiz numara kontrolü
- 📊 İlerleme durumu takibi

## Kurulum

1. Python 3.8 veya üstü sürümü yükleyin
2. Gerekli kütüphaneleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
3. Uygulamayı başlatın:
   ```
   python main2.py
   ```

## Kullanım

1. **Numara Ekleme**
   - "Numara Ekle" butonu ile tek tek numara ekleyebilirsiniz
   - "Numaraları İçe Aktar" ile txt dosyasından toplu numara ekleyebilirsiniz
   - Numaraları ülke kodu ile birlikte girin (örn: 905551234567)

2. **Medya Dosyaları**
   - "Dosya Ekle" butonu ile medya dosyaları ekleyebilirsiniz
   - Her medya için özel mesaj yazabilirsiniz
   - Mesaj eklenen medyalar yıldız işareti (⭐) ile gösterilir
   - Medya mesajları otomatik olarak kaydedilir

3. **Mesaj Gönderme**
   - Ana mesaj kutusuna göndermek istediğiniz mesajı yazın
   - Delay ve Wait sürelerini ayarlayın
   - "Gönderimi Başlat" butonuna tıklayın
   - İşlem durumunu "Durum" sekmesinden takip edin

## Ayarlar

- **Delay**: Mesajlar arası bekleme süresi (saniye)
- **Wait**: Elementlerin bulunması için gereken maksimum süre (saniye)
- Ayarlar otomatik olarak kaydedilir ve uygulama yeniden başlatıldığında yüklenir

## Güvenlik

- Numaralar settings.json dosyasına kaydedilmez
- Medya mesajları ve ayarlar yerel olarak saklanır
- WhatsApp Web oturumu kapatıldığında tüm veriler silinir


## Gereksinimler

- Python 3.8+
- PySide6
- Selenium
- Chrome WebDriver

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.
```

Bu README dosyası, projenin özelliklerini, kurulum ve kullanım talimatlarını, örnek kodları içermekte ve okuyucuların kolayca anlayabilmesi için yapılandırılmıştır. İstediğin gibi düzenlemeler yapabilirsin.



