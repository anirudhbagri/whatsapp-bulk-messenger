from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time
from urllib.parse import quote
import os 

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
options.add_argument('--start-maximized')
options.add_argument("--disable-background-timer-throttling")  # Arka planda zamanlayıcı kısıtlamalarını devre dışı bırak
options.add_argument("--disable-renderer-backgrounding")  # Arka planda render işlemlerini durdurmayı devre dışı bırak

import os
import glob

# Klasör yolunu belirle
klasor_yolu = r'C:\Users\TOM\Documents\Projeler\otonomwhatsapp\whatsapp-bulk-messenger'

# JPG ve PNG uzantılı tüm dosyaları bul ve listeye ekle
image_paths= glob.glob(os.path.join(klasor_yolu, "*.jpg")) + glob.glob(os.path.join(klasor_yolu, "*.png")) + glob.glob(os.path.join(klasor_yolu, "*.jpeg"))\
+glob.glob(os.path.join(klasor_yolu, "*.pdf"))\
+ glob.glob(os.path.join(klasor_yolu, "*.mp4"))

print(image_paths)

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# ------- Mesajınızın bulunduğu dosya ------------#
f = open("message.txt", "r", encoding="utf8")
img_message = f.read()
f.close()

f = open("message.txt", "r", encoding="utf8")
pdf_message = f.read()
f.close()

f = open("message.txt", "r", encoding="utf8")
video_message = f.read()
f.close()


# ----- Burada mesajınızı gösterir --------#
print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + img_message)
print("\n" + style.RESET)
message = quote(img_message)

# --------- Burada göndermek istediğiniz numaları dosyadan çeker ---------- # 

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()

# ----------- Burada Numara sayısını yani mesaj sayısını gösterir ----------- #

total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)


delay = 30 # Elemenlar bulmak için gereken süre 

# ----- Burada tarayıcıyı açar ------- #
svc = webdriver.ChromeService(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=svc,options=options)

print("Tarayıcınız açıldığında web whatsapp'ta oturum açın (bir kere yapmanız yeterli olacaktır.)")

driver.get('https://web.whatsapp.com') # web whatsapp sitesine gidilir. 

# -------- Burada whatsapp'a girdiğinizi onaylaylarsınız ------ #
input(style.MAGENTA + "Whatsapp Web'e giriş tamamlandıktan ve sohbetleriniz görünür hale geldikten sonra ENTER tuşuna basın..." + style.RESET)


# ---------------- Burada gönderme işlemleri yapılıyor ---------- #

for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
	try:
		

		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		
		for i in range(3):
			if not sent:
				driver.get(url)

				try:
					alert = driver.switch_to.alert  # Uyarıya geçiş yapın
					print(alert.text)  # Uyarı metnini (isteğe bağlı olarak) yazdırın
					alert.accept()  # Uyarıyı onaylayın
					print("Uyarı onaylandı.")
				except:
					print("Uyarı bulunamadı.")

				try:
					kontrol = 0
					for img in image_paths:
						if kontrol ==0:
							
							attach_button = WebDriverWait(driver, delay).until(
								EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='plus']"))
							)
							attach_button.click()
							time.sleep(0.5)
							# Dosya yükleme butonunu bul
							image_box = WebDriverWait(driver, delay).until(
								EC.presence_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"))
							)

							image_box.send_keys(os.path.abspath(img))
							
							time.sleep(2)
						else:
							attach_button = WebDriverWait(driver, delay).until(
								EC.presence_of_element_located((By.XPATH, "//input[@accept='*']"))
							)
							
							attach_button.send_keys(os.path.abspath(img))
							
							time.sleep(2)
						kontrol +=1
					
					
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
					time.sleep(2)
					
					
					
				except Exception as e:
					print(e)
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					click_btn.click()
					time.sleep(2)
					sent=True
					sleep(2)

					
					# Yükleme simgesi (circle) kaybolana kadar bekle
					WebDriverWait(driver, 3000000000).until_not(
						EC.presence_of_element_located((By.TAG_NAME, "circle"))
					)
					print(style.GREEN + 'Yükleme tamamlandı.' + style.RESET)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)

	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

# ------------ İşlemler bitince tarayıcı kapatılıyor --------------- #

driver.close()





