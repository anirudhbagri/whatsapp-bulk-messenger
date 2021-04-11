from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform

options = Options()

print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Anirudh Bagri     ******")
print("*****           www.github.com/anirudhbagri         ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")

f = open("message.txt", "r")
message = f.read()
f.close()

print("##########################################################")
print('This is your message..')
print(message)
print("##########################################################")
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
f.close()
total_number=len(numbers)
print("##########################################################")
print('\nWe found ' + str(total_number) + ' numbers in the file')
print("##########################################################")
print()
delay = 30

if platform == "win32":
	driver = webdriver.Chrome("drivers\\chromedriver.exe", options=options)
else:
	driver = webdriver.Chrome("./drivers/chromedriver", options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable	.")
for idx, number in enumerate(numbers):
	if number == "":
		continue
	print('{}/{} => Sending message to {}.'.format((idx+1), total_number, number))
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		driver.get(url)
		try:
			click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_1E0Oz')))
		except (UnexpectedAlertPresentException, NoAlertPresentException) as e:
			print("alert present")
			Alert(driver).accept()
		sleep(1)
		click_btn.click()
		sleep(3)
		print('Message sent to: ' + number)
	except Exception as e:
		print('Failed to send message to ' + number + str(e))
