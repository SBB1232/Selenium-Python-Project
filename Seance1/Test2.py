# Test Case
# -------------
# 1 Ouvrir le navigateur Chrome
# 2 Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
# 3 Entrer username Admin
# 4 Entrer password admin123
# 5 Cliquer sur le bouton login
# 6 Recuperer le titre de la page (titre actuel)
# 7 Vérifier que le titre de la page : OrangeHRM (attendu)
# 8 Fermer le navigateur
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 1 Ouvrir le navigateur Chrome
driver = webdriver.Chrome()
# Agrandir la fenetre
driver.maximize_window()
# 2 Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
driver.get("https://opensource-demo.orangehrmlive.com/")
# 3 Entrer username Admin
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# 4 Entrer password admin123
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# 5 Cliquer sur le bouton login
driver.find_element(By.ID, "btnLogin").click()
# Laisser la page ouverte pour 4 secondes
time.sleep(4)
# 6 Recuperer le titre de la page (titre actuel)
titre_actuel = driver.title
# 7 Vérifier que le titre de la page : OrangeHRM (attendu)
if titre_actuel == "OrangeHRM":
    print("Le titre est correct")
else:
    print("Le titre est différent")
# Laisser la page ouverte pour 4 secondes
time.sleep(4)
# 8 Fermer le navigateur
driver.close()

