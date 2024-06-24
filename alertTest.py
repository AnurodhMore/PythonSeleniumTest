import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name="Anurodh"
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID,"name").send_keys(name)

driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()

assert name in alertText