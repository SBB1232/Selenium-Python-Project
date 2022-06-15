# Test case 1
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
# Cliquer sur le lien Register
driver.find_element(By.LINK_TEXT, "Register").click()
# Remplir le champ Firstname
driver.find_element(By.ID, "FirstName").send_keys("Sana")
# Remplir le champ Lastname
driver.find_element(By.NAME, "LastName").send_keys("Benboubaker")
# Remplir le champ email
driver.find_element(By.ID, "Email").send_keys("sana@sana.com")
# Remplir le champ Password
driver.find_element(By.NAME, "Password").send_keys("123456789")
# Remplir le champ ConfirmPassword
driver.find_element(By.ID,"ConfirmPassword").send_keys("123456789")
# A^ppuyer sur le bouton Register
driver.find_element(By.ID, "register-button").submit()
# temps d'arret de 4 secondes
time.sleep(4)
# fermer le navigateur
driver.close()