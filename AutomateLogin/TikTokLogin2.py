from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

username = '.......' #The username is hidden.
password = '.......' #The password is hidden.

#https://stackoverflow.com/questions/76928765/attributeerror-str-object-has-no-attribute-capabilities-in-selenium
chrome_service = Service(executable_path='/Users/ada1/chromedriver')
driver = webdriver.Chrome(service=chrome_service)
driver.get('https://www.tiktok.com')
driver.find_element(By.XPATH, '//div/div/div/button[@id="header-login-button"]').click()
driver.find_element(By.XPATH, "//div[contains(text(), 'Use phone / email / username')]").click()
driver.find_element(By.XPATH, '//form/div/a[@class="ep888o80 css-1mgli76-ALink-StyledLink epl6mg0"]').click()
driver.find_element(By.NAME, 'username').send_keys(username)
driver.find_element(By.XPATH, '//form/div/div/input[@type="password"]').send_keys(password)
driver.find_element(By.XPATH, '//button[@class="e1w6iovg0 css-11sviba-Button-StyledButton ehk74z00"]').click()
time.sleep(60)

print('Logged in successfully!')