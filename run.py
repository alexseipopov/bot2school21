import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .config import *

driver = webdriver.Chrome("Путь к файлу хромиума, желательно положить в этой же директории")
driver.get('https://applicant.21-school.ru')

email = driver.find_element(By.ID, 'email')
password_f = driver.find_element(By.ID, 'password')

email.send_keys(EMAIL)
password_f.send_keys(PASSWORD, Keys.ENTER)

while True:
    time.sleep(5)
    lines = driver.find_elements(By.CSS_SELECTOR, 'tr>td:nth-child(2)')
    
    for j, i in enumerate(lines):
        i_ = int(i.text.split()[0])
        if i_ > 0:
            buttons = driver.find_elements(By.CSS_SELECTOR, '.item__column.action')
            buttons[j].click()
            print("SUCCESS")
            sys.exit()
    time.sleep(15)
    driver.refresh()