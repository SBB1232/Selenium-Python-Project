import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(2)
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("classFrame")   # peut le nom ou l id du frame
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

time.sleep(2)
driver.quit()