# Test Case

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Ouvrir le navigateur Chrome
driver = webdriver.Chrome()
# Agrandir la fenetre
driver.maximize_window()
# Accèder à l'url https://www.google.ca/?hl=fr
driver.get("https://www.google.ca/?hl=fr")
# Saisir "selenium " dans la barre de recherche
driver.find_element(By.NAME, "q").send_keys("selenium")
# Identifier les éléments de la liste des résultats
print(driver.find_elements(By.XPATH, "//div[@class='aajZCb']//li"))
print(len(driver.find_elements(By.XPATH, "//div[@class='aajZCb']//li")))


# for i in range(1,11):
#     result.find_elements(By.XPATH, "")

# for i in range(1,11):
#     if driver.find_element(By.XPATH, "//div[@class='aajZCb']//li[i]") == "selenium webdriver":
#         print("OK")
#         break
#     else:
#         print("NOK")







# Laisser la fenetre ouverte pour 2 secondes
time.sleep(2)
# fermer la fenetre
driver.close()




