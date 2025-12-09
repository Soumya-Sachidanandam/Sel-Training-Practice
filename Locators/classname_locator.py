import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/register')
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.find_element('class name','text-box.single-line').send_keys('soumya')