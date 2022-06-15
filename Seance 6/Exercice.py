# Test Case

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Ouvrir une instance chrome
driver = webdriver.Chrome()
# Agrandir la fenetre de chrone
driver.maximize_window()
# Accéder à l'url http://omayo.blogspot.com/
driver.get("http://omayo.blogspot.com/")
# Identifier l'élément qui contient la liste 1
menu1 = driver.find_element(By.ID, "multiselect1")
# Appeler la classe Select qui permet de selectionner un élément dans une liste
detail_menu1 = Select(menu1)
# Ne rien faire pendant 2 secondes
time.sleep(2)
# Choisir l'élément Hyundai de la liste
detail_menu1.select_by_value("Hyundaix")
# Ne rien faire pendant 2 secondes
time.sleep(2)
# Choisir l'élément Audi de la liste
detail_menu1.select_by_value("audix")
# récupérer toutes les options du menu
all_options_menu1 = detail_menu1.options
# récupérer la longueur de la liste
longueur1 = len(all_options_menu1)
print("La longueur de la 1ère liste est ", longueur1)
# Afficher les éléments de la 2ème liste
print("Les options de la 1ère liste sont : ")
for option in all_options_menu1:
    print(option.text)
# Identifier l'élément qui contient la liste 2
menu2 = driver.find_element(By.ID, "drop1")
# Appeler la classe Select qui permet de selectionner un élément dans une liste
detail_menu2 = Select(menu2)
# Ne rien faire pendant 2 secondes
time.sleep(2)
# Choisir l'élément doc3 de la liste
detail_menu2.select_by_visible_text("doc 3")
# récupérer toutes les options du menu
all_options_menu2 = detail_menu2.options
# récupérer la longueur de la liste
longueur2 = len(all_options_menu2)
print("La longueur de la 2ème liste est ", longueur2)
# Afficher les éléments de la 2ème liste
print("Les options de la 2ème liste sont : ")
for option in all_options_menu2:
    print(option.text)
# Ne rien faire pendant 2 secondes
time.sleep(2)
# Déselectionner l'élément Hyundai de la 1ere liste
detail_menu1.deselect_by_visible_text("Hyundai")
# Ne rien faire pendant 2 secondes
time.sleep(2)
# Déselectionner l'élément Audi de la 1ere liste
detail_menu1.deselect_by_visible_text("Audi")
# Laisser la fenetre ouverte pour 2 secondes
time.sleep(2)
# Fermer la fenetre
driver.close()
