# Test case 2
# Lancer le navigateur
# Accéder à https://demo.nopcommerce.com/
# Cliquer sur le lien Register
# Remplir le formulaire
# Cliquer sur le bouton Register
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Créer une instance de chrome vide
driver = webdriver.Chrome()
# Agrandir la fenêtre de chrome
driver.maximize_window()
# Accéder a l'url
driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.LINK_TEXT, "Log in").click()
driver.find_element(By.CLASS_NAME, "email").send_keys("sana@sana.com")
driver.find_element(By.ID, "Password").send_keys("123456789")
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").submit()
# temps d'arret de 4 secondes
time.sleep(4)
# fermer le navigateur
driver.close()