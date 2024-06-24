import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name="Anurodh"
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)

assert count > 0

for result in results:
    result.find_element(By.XPATH,"div/button").click()

#driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
time.sleep(6)
print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)

