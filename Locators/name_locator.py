import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('name','firstname').send_keys('soumya')
time.sleep(2)
driver.find_element('name','lastname').send_keys('s')
time.sleep(2)
driver.find_element('name','reg_email__').send_keys('9899898')
time.sleep(2)
driver.find_element('name','reg_passwd__').send_keys('hjshdjshdjs')
time.sleep(2)
