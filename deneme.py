
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path=r'C:/Users/TOM/Desktop/chromedriver.exe')
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


options.add_argument(f"--user-data-dir={base_dir}")
options.add_argument('--start-maximized')
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-renderer-backgrounding")

driver = webdriver.Chrome( options=options)
driver.get("https://web.whatsapp.com")

contact_name = 'Contact Name'
message = 'Hello, this is an automated message.'

time.sleep(15)  # Wait for the user to scan the QR code and log in
# Find the contact/group and open the chat
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(contact_name)
search_box.send_keys(Keys.ENTER)

# Send the message
message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)

# Wait and close the browser
time.sleep(5)
driver.quit()



file_inputs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//input[@type='file']")
    )
)

media_input = file_inputs[1]  # genelde medya input ilk olur

time.sleep(2)
pyautogui.write('"C:\\Users\\TOM\\Downloads\\Gemini_Generated_Image_gkig9sgkig9sgkig (1).png"') # Dosya yolunu yazar
time.sleep(0.5)
pyautogui.press('enter')'C:\Users\TOM\Downloads\Gemini_Generated_Image_gkig9sgkig9sgkig (1).png'