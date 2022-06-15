import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[contains(text(), 'Prompt')]").click()
time.sleep(2)
# Récupérer le prompt et switcher vers le prompt
promptWindow = driver.switch_to.alert
# Récupérer le texte du prompt
message = promptWindow.text
print(message)
# Répondre sur la fenetre prompt
promptWindow.send_keys("Yes")
time.sleep(2)
# cliquer sur OK
promptWindow.accept()
# cliquer sur annuler sur la JS prompt
# driver.find_element(By.XPATH, "//button[contains(text(), 'Prompt')]").click()
# promptWindow.dismiss()
time.sleep(2)
driver.quit()