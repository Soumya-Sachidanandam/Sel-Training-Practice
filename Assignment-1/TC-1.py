import time
from selenium import webdriver
c_driver=webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)



driver.get("https://www.agoda.com/en-in")