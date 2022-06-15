# Test Case
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ouvrir le navigateur Chrome
driver = webdriver.Chrome()
# Naviguer sur l'url https://login.salesforce.com/?locale=fr-ca
driver.get("https://login.salesforce.com/?locale=fr-ca")
# Agrandir la fenetre
driver.maximize_window()
# Saisir l'user name
driver.find_element(By.ID, "username").send_keys("sana")
# Saisir le mdp
driver.find_element(By.ID, "password").send_keys("Sana")
# Cliquer sur login
driver.find_element(By.ID, "Login").click()
# Récupérer le titre de la page
titre_page = driver.title
# Afficher le titre de la page
print("Le titre de la page est : ",titre_page)
# Récupérer le message d'erreur
message = driver.find_element(By.ID, "error").text
# Afficher le message d'erreur
print("Le message d'erreur est : ", message)
# Laisser la fenetre ouverte pour 2 secondes
time.sleep(2)
# Fermer le navigateur
driver.close()
