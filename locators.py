import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("anurodhmore18@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Anurodh18")
driver.find_element(By.ID,"exampleCheck1").click()

#Static Dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)


driver.find_element(By.XPATH,"//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
time.sleep(2)