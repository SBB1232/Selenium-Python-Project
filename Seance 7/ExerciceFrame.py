import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Frames.html")
time.sleep(2)
# Localiser le premier lien : Single Iframe
driver.find_element(By.XPATH, "//a[contains(text(), 'Single')]").click()
driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Sana")
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'with')]").click()
# Localiser le deuxiéme lien : Iframe With in an Iframe
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']"))
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']"))
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Benboubaker")
time.sleep(2)
# Retour à la page initiale
driver.switch_to.parent_frame()
driver.switch_to.default_content()
time.sleep(2)
driver.quit()

