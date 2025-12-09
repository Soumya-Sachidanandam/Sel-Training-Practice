import time

'''         using time.sleep()          '''


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\Ramya-Notes\loading.html')
# time.sleep(20)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Chandana')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Thandlam')

#####################################################################################################################################
'''
using implicitly_wait()

'''

import time
from selenium import webdriver

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\Ramya-Notes\loading.html')
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Chandana')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Thandlam')


#########################################################################################################################################

'''
explicit_wait

'''

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 30)
#
# driver.get(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\Ramya-Notes\loading.html')
#
# wait_.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Chandana')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Thandlam')


#####################################################################################################################################
'''
Ex:Explicit wait 
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauceeeee')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(2)

##------------------------------------------------------------------------------------

# ## condition1. Took the url to check whether the login is successful or not----url_contains()
# try:
#     wait_.until(expected_conditions.url_contains('inventory'))
#     print("Successful login")
# except:
#     print("Unsuccessful login")

##------------------------------------------------------------------------------------

# ## condition2. Took some element on the homepage and checking if that element is visible or not
# try:
#     wait_.until(expected_conditions.visibility_of_element_located(('xpath', '(//button[text()="Add to cart"])[1]')))
#     print("Successful login")
# except:
#     print("Unsuccessful login")

###################################################################################################################################3
'''
1st way: increasing time.sleep()
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\Ramya-Notes\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(45)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

####################################################################################################################################3

'''
implicitly_wait()
'''
#
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(50)
#
# driver.get(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\Ramya-Notes\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# driver.find_element('xpath', '//div[text()="100%"]')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

##########################################################################################################################################

'''
explicit_wait
'''


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 50)
#
# driver.get(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\Ramya-Notes\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# wait_.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

#########################################################################################################################################
'''
Ex for explicit wait with condition of checking alert box and then performing the operation 
'''

'''
own-combines scroll code here
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
#
# ref_ele=driver.find_element("xpath","//button[@id='PopUp']")
# ac_obj.scroll_to_element(ref_ele).perform()
#
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# assert wait_.until(expected_conditions.alert_is_present())  #assert condition(message)  #if true it executes statement
#                                                             # block else throws assertion error
# alert_obj = driver.switch_to.alert
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()


#########################################################################################################################################
##-----Using invisibility_of_element()---##

#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
# time.sleep(2)
#
# wait_.until(EC.element_to_be_clickable(('xpath', '//button[text()="Start"]'))).click()
#
# start = time.time()
# wait_.until(EC.invisibility_of_element(('xpath', '//div[text()="Loading... "]')))
# end = time.time()
#
# print(end-start)










