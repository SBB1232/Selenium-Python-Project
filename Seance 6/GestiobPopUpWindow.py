import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# admin:admin pour contourner le fait de taper ds les 2 champs du pop up
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(2)
driver.quit()