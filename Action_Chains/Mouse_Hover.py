'''
Mouse hover on each and every element in Myntra: Men,women,kids, till genZ but not studio
'''
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)

navigation=driver.find_elements("xpath","//a[@class='desktop-main']")

##-------Solution-1------#######

# for navi in navigation[:-1]:
#
#     ac_obj.move_to_element(navi).perform()
#     time.sleep(2)

##----Solution-2------#####


# for navi in range(0,len(navigation)-1):
#     ac_obj.move_to_element(navigation[navi]).perform()
#     time.sleep(2)
#####--------------------Eg -2-----------------#

driver.get('https://www.kushals.com/')
time.sleep(4)

accessories = driver.find_element('xpath', '(//a[contains(text(), "Accessories")])[2]')
ac_obj.move_to_element(accessories).perform()
time.sleep(2)

wedding_store = driver.find_element('xpath', '(//a[contains(text(), "Wedding Store")])[2]')
ac_obj.move_to_element(wedding_store).perform()