import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Ouvrir une instance de chrome
driver = webdriver.Chrome()
# Agrandir la fenetre
driver.maximize_window()
# naviguer a l url https://www.opencart.com/index.php?route=account/register
driver.get("https://www.opencart.com/index.php?route=account/register")
# identifier l'elment qui contient toute la liste
menu = driver.find_element(By.ID, "input-country")
# appel a une classe selenium Select qui permet de selectionner un element dans une liste
pays = Select(menu)    # Select prend en parametre l element qu on va itérer
# selectionner une option de la liste
# pays.select_by_visible_text("Tunisia")  # selection par texte visible
# pays.select_by_value("214")  # selection par value
# selection par index uniquement qd la liste est figée
pays.select_by_index(216)
# recuprer toutes les options dans select
toute_options = pays.options
# afficher nombre d options
nombre = len(toute_options)
print(nombre)
# for option in toute_options:
#     print(option.text)

for option in toute_options:
    if option.text == "Canada":
        option.click()
        break

time.sleep(2)
driver.close()