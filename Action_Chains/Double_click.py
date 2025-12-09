import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

dc=driver.find_element("xpath","//label[text()='Name:']")
ac_obj.double_click(dc).perform()

# copy_ele=driver.find_element("xpath","//button[text()='Copy Text']")
#
# ac_obj.double_click(copy_ele).perform()

