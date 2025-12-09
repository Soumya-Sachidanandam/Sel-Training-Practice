import time

'''         using time.sleep()          '''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\loading.html')
time.sleep(20)

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Chandana')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('Thandlam')

#####################################################################################################

'''         implicit_wait         '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\loading.html')
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Chandana')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Thandlam')

#####################################################################################################

'''         explicit_wait         '''
#
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
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\loading.html')
#
# wait_.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Chandana')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Thandlam')





















