from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
## if cannot read from /var/tmp/chrome_user_data error uncomment below line
##options.add_argument("user-data-dir=C:\environments\selenium")
## If binary error occur uncomment this
##options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"

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
print(style.RESET)

with open("message.txt", "r", encoding="utf8") as f:
    message = f.read()
    ## if location is in text message it means you have to attach that image
    if "location=" in message:
        message_data = message.split("location=")
    else:
        message_data = [message]
print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message_data[0])
print("\n" + style.RESET)
numbers = []
with open("numbers.txt", "r") as f:
    numbers.extend(
        line.strip() for line in f.read().splitlines() if line.strip() != ""
    )
total_number = len(numbers)
print(style.RED + 'We found ' + str(total_number) +
      ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				## First trying sending the image
				if len(message_data)>1:
					try:
						click_attach = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
						click_attach.click()
						upload_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input")))
						upload_button.send_keys(message_data[1])
						# button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span")
						button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span")))
						button.click()
						print(style.GREEN + 'Image sent to: ' + number + style.RESET)
					except Exception as e:
						print(style.RED + 'Failed to send image to ' + number + str(e) + style.RESET)
				## clicking on the message box and sending text message
				try:
					sleep(3)
					type = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")))
					type.send_keys(message_data[0].replace('\n', ' '))
					type.send_keys(Keys.ENTER)
				except Exception as e:
					print(style.RED +
					      f"\nFailed to send message to: {number}, retry ({i+1}/3)")
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
				else:
					sleep(1)
					sent = True
					type.send_keys(Keys.ENTER)
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
driver.close()
