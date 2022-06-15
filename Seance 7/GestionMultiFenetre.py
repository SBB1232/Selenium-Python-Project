import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# Récupérer l ID de la fenetre ouverte chaque fenetre a un id unique)
parentWindowId = driver.current_window_handle  # pour une seule fenetre
print(parentWindowId)
# CDwindow-305EF8E7403A392428180CA61715BCB3
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
# recuperer une liste d'ID
windowHandlesIds = driver.window_handles
parentWindowId = windowHandlesIds[0]
childWindowId = windowHandlesIds[1]
print("parent Window Id est : ", parentWindowId)
print("child Window Id est : ", childWindowId)  # CDwindow-C8FABADB15B93173F90DB7E01158613C
# a chaque exécution l id change

driver.switch_to.window(childWindowId)  # la parametre est l id
urlCourant = driver.current_url
print(urlCourant)
titre1 = driver.title
print(titre1)

# 2eme approche

for winid in windowHandlesIds:
    driver.switch_to.window(winid)
    if driver.title == titre1:
        driver.close()

time.sleep(3)
driver.quit()

