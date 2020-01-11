from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from urllib.parse import quote

options = Options()
#options.add_argument("user-data-dir=/tmp/tarun")
#options.add_argument("user-data-dir=C:\\Users\\anirudh_bagri\\AppData\\Local\\Google\\Chrome\\User Data")

f = open("message.txt", "r")
message = f.read()
f.close()
print('This is your message:')
print(message)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
f.close()
print('\nWe found ' + str(len(numbers)) + ' numbers in the file')
delay = 30

print('Once your browser opens up, make sure you sign in to web whatsapp and then press enter')
driver = webdriver.Chrome("drivers\\chromedriver.exe", chrome_options=options)
driver.get('https://web.whatsapp.com')
input()
for number in numbers:
	if number == "":
		continue
	print('Sending message to: ' + number)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		driver.get(url)
		click_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME , '_3M-N-')))
		click_btn.click()
		sleep(1)
		print('Message sent to: ' + number)
	except Exception:
		print('Failed to send message to ' + number)