import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[contains(text(), 'Alert')]").click()
time.sleep(2)
# Récupérer l'alerte et switcher vers l alerte
alertWindow = driver.switch_to.alert
# Récupérer le texte de l alerte
message = alertWindow.text
print(message)
# cliquer sur ok de l alerte
alertWindow.accept()
time.sleep(2)
driver.quit()