
'''
Here we are creating
def handling_windows():
    return driver.window_handles because once the function is loaded into the memory it is easy for the interpreter
    to get it whenever it is called rather than to write repeated code multiple times
'''

'''
ex-1: Here we are launching the website and after scrolling till g+ we are clicking on it
'''
#
#
# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
#
# def handling_windows():
#     return driver.window_handles
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys('Google pixel9')
#         time.sleep(2)
#         driver.switch_to.window(handling_windows()[0])
#         time.sleep(1)
#
#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'x.com' in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()



'''
Ex-2
'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)


#Launching app
driver.get('https://www.flipkart.com/')
time.sleep(2)

#Locating Search bar and entering data
driver.find_element('xpath','//input[@title="Search for Products, Brands and More"]').send_keys("Phones under 30000")
time.sleep(2)

#Locating search button
driver.find_element('xpath','//button[@title="Search for Products, Brands and More"]').click()
time.sleep(2)

#Locating the first phone
driver.find_element('xpath','//div[@class="KzDlHZ"]').click()
time.sleep(2)


def handle_windows():
    return driver.window_handles


#If the first phone contains the below mentioned text then item should be added to cart

for handle in handle_windows():
    driver.switch_to.window(handle)
    time.sleep(2)
    if 'samsung-galaxy-f36-5g-red-128-gb' in driver.current_url:
        driver.find_element('xpath','//button[text()="Add to cart"]').click()
        time.sleep(2)


#Else locate help centre at the bottom and click on it
driver.find_element('xpath','//span[text()="Help Center"]').click()
time.sleep(2)


#click on Know more
for handle in handle_windows():
    driver.switch_to.window(handle)
    time.sleep(2)
    if 'helpcentre' in driver.current_url:
        driver.find_element('xpath','//a[text()="Know more"]').click()



















