# Test case
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Ouvrir le navigateur Chrome
driver = webdriver.Chrome()
# Agrandir la fenetre
driver.maximize_window()
# Accéder à l'url https://www.opencart.com/index.php?route=account/register
driver.get("https://www.opencart.com/index.php?route=account/register")
# sélectionner le pays Tunisia
dropCountry = driver.find_element(By.ID, "input-country")
country = Select(dropCountry)
# country.select_by_visible_text("Tunisia")
# country.select_by_index(216)
country.select_by_value("214")
allOptions = country.options
totalOptions = len(allOptions)
print("Le nombre total des pays est : ", totalOptions)
# for i in allOptions:
#     print(i.text)

for i in allOptions:
    if i.text == "Canada":
        i.click()
        break
# Laisser la fenetre ouverte pour 3 secondes
time.sleep(3)
# fermer la fenetre
driver.close()

