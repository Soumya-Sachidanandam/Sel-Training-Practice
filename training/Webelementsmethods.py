import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
f_driver=webdriver.Chrome(opts)

driver=webdriver.Chrome(opts)
driver.get("https://www.instagram.com/")
time.sleep(3)