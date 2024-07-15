from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

phoneNumber = '12345678900'
verificationCode = '123456'

chrome_service = Service(executable_path='/Users/ada1/chromedriver')
driver = webdriver.Chrome(service=chrome_service)
driver.get('https://www.xiaohongshu.com')
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//div/button[@id="login-btn"]'))
driver.find_element(By.XPATH, '//form/label/input[@type="text"]').send_keys(phoneNumber)
driver.find_element(By.XPATH, '//form/label/input[@type="number"]').send_keys(verificationCode)
driver.find_element(By.XPATH, '//div[@class="icon-wrapper"]').click()
time.sleep(60)
driver.find_element(By.XPATH, '//button[@class="submit"]').click()
time.sleep(600)


