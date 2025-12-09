

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(1)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(1)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys('Ganga')
# driver.find_element('id', 'LastName').send_keys('Shintre')
# driver.find_element('id', 'Email').send_keys('ganga@gmail.com')
# driver.find_element('id', 'Password').send_keys('ganga@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('ganga@12345')


###############################################################################################################################


import time
from selenium import webdriver
from DataDrivenTesting.read_excel_demo import reading_testdata

path=r'C:\Users\Naveen\PycharmProjects\Selenium_Training\DataDrivenTesting\TestData.xlsx'

for i in range(1,5):

    data=reading_testdata(path,'reg')


## data = {'firstname': 'Ganga', 'lastname': 'Shintre', 'email_id': 'ganga@gmail.com', 'pwd': 'ganga@12345', 'confirm_pwd': 'ganga@12345'}

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(1)
#
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(1)
# driver.find_element('id', 'gender-female').click()
# driver.find_element('id', 'FirstName').send_keys(data['firstname'])
# driver.find_element('id', 'LastName').send_keys(data['lastname'])
# driver.find_element('id', 'Email').send_keys(data['email_id'])
# driver.find_element('id', 'Password').send_keys(data['pwd'])
# driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])
# driver.find_element('id', 'register-button').click()



##############################################################################################################

#own---to take inputs one after other--mam told she will give other code

# for i in range(1,5):
#         driver.get('https://demowebshop.tricentis.com/')
#         driver.maximize_window()
#         time.sleep(1)
#
#         driver.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(1)
#         driver.find_element('id', 'gender-female').click()
#         driver.find_element('id', 'FirstName').send_keys(data['firstname'])
#         driver.find_element('id', 'LastName').send_keys(data['lastname'])
#         driver.find_element('id', 'Email').send_keys(data['email_id'])
#         driver.find_element('id', 'Password').send_keys(data['pwd'])
#         driver.find_element('id', 'ConfirmPassword').send_keys(data['confirm_pwd'])
#         driver.find_element('id', 'register-button').click()
#
#         driver.find_element('xpath', '//a[text()="Log out"]').click()



































