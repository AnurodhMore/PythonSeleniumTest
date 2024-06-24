import time

from selenium import webdriver

#service_obj = Serive("User/Amrore/chromdriver.exe")
# driver = webdriver.Chrome(service=service_obj)


#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://www.flipkart.com/?affid=affsiteplug&affExtParam1=356aad1f48a72d1a94b95328eb355f7b&affExtParam2=60827")
driver.maximize_window()
print(driver.title)
print(driver.current_url)