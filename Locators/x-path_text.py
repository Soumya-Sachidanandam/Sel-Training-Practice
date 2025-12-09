import time

from selenium import webdriver
c_driver=webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get("https://www.amazon.in/")
time.sleep(3)

driver.find_element("xpath",'''//a[text()="Today's Deals"]''').click()
time.sleep(3)

driver.find_element("xpath","//button[text()='Coupons']").click()
time.sleep(3)

driver.find_element("xpath","//span[text()='Appliances']").click()
time.sleep(3)