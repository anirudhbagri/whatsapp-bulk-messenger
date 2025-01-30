from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
from time import sleep
from urllib.parse import quote
import os

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

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

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Anirudh Bagri     ******")
print("*****           www.github.com/anirudhbagri         ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print("*********************Modified By Jaush********************")
print("*****************https://github.com/J4USH*****************")
print(style.RESET)

f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()
image_path='<Enter the absolute path>\whatsapp-bulk-messenger\RickRoll.jpeg'

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

chromedriver_autoinstaller.install()

# Initialize WebDriver
driver = webdriver.Chrome()

print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
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
					pass
					
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					attachment_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-icon='plus']")))
					attachment_btn.click()
					sleep(1)
					image_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")))
					image_input.send_keys(image_path)
					sleep(3)
					send_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-icon='send']")))
					send_btn.click()
        
					# click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
driver.close()
