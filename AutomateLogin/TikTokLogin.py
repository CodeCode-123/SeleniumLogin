from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = '......' #The username is hidden.
password = '......' #The password is hidden.

#https://stackoverflow.com/questions/76928765/attributeerror-str-object-has-no-attribute-capabilities-in-selenium
chrome_service = Service(executable_path='/Users/ada1/chromedriver')
driver = webdriver.Chrome(service=chrome_service)
driver.get('https://www.tiktok.com/login/phone-or-email/email')
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.CSS_SELECTOR, 'input[type=\"password\" i]').send_keys(password)
driver.find_element(By.XPATH, '//button[@class="e1w6iovg0 tiktok-11sviba-Button-StyledButton ehk74z00"]').click()
time.sleep(60)
#https://stackoverflow.com/questions/75569829/how-to-slowly-move-a-slider-with-selenium
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(By.XPATH, '//span[@class="sc-ckVGcZ cpOoXK"]'))
slider = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(By.XPATH, '//span[@class="sc-ckVGcZ cpOoXK"]'))
ActionChains(driver).drag_and_drop_by_offset(slider, 250, 0).perform()
time.sleep(600)

print('Logged in successfully!')





