import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
# driver.find_element('name', 'username').send_keys('Vidhyalakshmi')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('vidhya@12345')
# time.sleep(1)

####################################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('name', 'firstname').send_keys('Pooja')
time.sleep(1)
driver.find_element('name', 'lastname').send_keys('Nokhwal')
time.sleep(1)
driver.find_element('name', 'reg_email__').send_keys('pooja@gmail.com')
time.sleep(1)
driver.find_element('name', 'reg_passwd__').send_keys('pooja@12345')
















































