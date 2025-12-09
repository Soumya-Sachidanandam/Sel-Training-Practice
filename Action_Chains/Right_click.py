'''

 We use context_click() to achieve right click
'''

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

right_click=driver.find_element("xpath","//h2[text()='Static Web Table']")
ac_obj.context_click(right_click).perform()