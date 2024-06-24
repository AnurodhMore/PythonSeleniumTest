import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

print(driver.title)

driver.find_element(By.ID,"autosuggest").click()
time.sleep(2)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for i in countries:
    if i.text == "India":
        i.click()
        time.sleep(2)
        break
#if you dynamically update the script, you can extract the text by getattribute
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"