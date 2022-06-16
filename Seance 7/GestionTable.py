import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
lignes = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
print("Nombre de lignes est :", len(lignes))
colonnes = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th")
print("Nombre de colonnes est :", len(colonnes))
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[3]/td[1]")  # //table[@name='BookTable']//tr[3]/td[1]
# //td[contains(text(), 'Learn Java')]
print(data.text)
# for i in lignes:
#     print(i.text)

time.sleep(4)
driver.quit()
