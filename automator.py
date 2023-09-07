from time import sleep
from urllib.parse import quote
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium options
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

# Define text styles for printing messages
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

# Print welcome message
print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by SeeSoft Devlopers ******")
print("*****      taking inspiration from Anirudh Bagri     ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

# Read the message from a file
f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

# Print the message
print(style.YELLOW + '\nThis is your message:')
print(style.GREEN + message)
print("\n" + style.RESET)

# URL-encode the message
message = quote(message)

# Read phone numbers from a file
numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number = len(numbers)

# Print the total number of phone numbers
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)

# Set the delay for WebDriverWait
delay = 30

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up, sign in to WhatsApp Web')
driver.get('https://web.whatsapp.com')

# Wait for user confirmation
input(style.MAGENTA + "After logging into WhatsApp Web and your chats are visible, press ENTER..." + style.RESET)

# Loop through the phone numbers and send messages
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        driver.get(url)
        sleep(5)  # Wait for WhatsApp Web to load

        # Locate the input field and send the message
        input_field = driver.find_element_by_css_selector('div[contenteditable="true"]')
        input_field.send_keys(message)

        # Locate the "Send" button and click it
        send_button = driver.find_element_by_css_selector('span[data-icon="send"]')
        send_button.click()
        
        sleep(2)  # Wait for the message to be sent

        print(style.GREEN + 'Message sent to: ' + number + style.RESET)
    except Exception as e:
        print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)

# Close the WebDriver
driver.close()