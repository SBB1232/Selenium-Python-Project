# Test case

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Créer une instance de chrome vide
driver = webdriver.Chrome()
# Agrandir la fenêtre de Chrome
driver.maximize_window()
# Accéder à l'URL
driver.get("https://www.saucedemo.com/")
# Remplir le premier champ User Name
driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
# Remplir le deuxiéme champ Password
driver.find_element(By.ID, "password").send_keys("secret_sauce")
# Valider sur le bouton Login
driver.find_element(By.ID, "login-button").submit()
# Ajouter un article au panier
driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
# Accéder au panier
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
# Temps d'arrêt de 4 secondes
time.sleep(4)
# Cliquer sur Remove
driver.find_element(By.NAME, "remove-sauce-labs-backpack").click()
# Cliquer sur Checkout
driver.find_element(By.ID, "checkout").click()
# Temps d arrêt de 4 secondes
time.sleep(4)
# Fermer le navigateur
driver.close()

