import time

from selenium import webdriver

# creer un objet de type chromeOptions
ops = webdriver.ChromeOptions()
# argument pour desactiver les notif
ops.add_argument("--disable-notification")

driver = webdriver.Chrome(options=ops)   # exécuter chrome en prenant en consideration les parametres
driver.maximize_window()
driver.get("https://whatmylocation.com/")





time.sleep(4)
driver.quit()