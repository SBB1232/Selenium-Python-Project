# Test case 1
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# Obtenir l url actuel de la page
driver.get("https://demo.nopcommerce.com/")
urlPage = driver.current_url
print(urlPage)
# Obtenir le titre de la page
titrePage = driver.title
print(titrePage)
# Obtenir le code source de la page
sourcePage = driver.page_source
print(sourcePage)

time.sleep(4)
driver.close()

