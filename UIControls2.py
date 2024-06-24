import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioBtn = driver.find_elements(By.XPATH,"//input[@type='radio']")
radioBtn[1].click()
assert radioBtn[1].is_selected()

buttons = driver.find_elements(By.XPATH,"//input[@type='radio']")

for button in buttons:
    if button.get_attribute("value")=="radio3":
        button.click()
        assert button.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
