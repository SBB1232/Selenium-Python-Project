
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
time.sleep(4)
driver.get("https://www.google.com")
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(4)
driver.refresh()
time.sleep(4)
driver.close()
