import os
import glob

# Klasör yolunu belirle
klasor_yolu = r'C:\Users\TOM\Documents\Projeler\otonomwhatsapp\whatsapp-bulk-messenger'

# JPG ve PNG uzantılı tüm dosyaları bul ve listeye ekle
image_paths= glob.glob(os.path.join(klasor_yolu, "*.jpg")) + glob.glob(os.path.join(klasor_yolu, "*.png")) + glob.glob(os.path.join(klasor_yolu, "*.jpeg"))\
+glob.glob(os.path.join(klasor_yolu, "*.pdf"))\
+ glob.glob(os.path.join(klasor_yolu, "*.mp4"))

# Listeyi yazdır
print(image_paths)