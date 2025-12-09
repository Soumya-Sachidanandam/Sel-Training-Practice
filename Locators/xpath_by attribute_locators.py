import time

from selenium import webdriver
c_driver=webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
#
# driver.get("https://www.apple.com/")
# time.sleep(2)
#
# driver.find_element("link text","Mac").click()


#
# driver.get("https://www.amazon.in/")
# time.sleep(3)
# driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("mobiles under 50000")
# driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()


driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)

driver.maximize_window()

driver.find_element("xpath","//a[@href='/register']").click()
time.sleep(3)


driver.find_element("xpath","//label[@for='gender-female']").click()
time.sleep(3)

driver.find_element("xpath","//input[@id='FirstName']").send_keys("Soumya")
time.sleep(3)

driver.find_element("xpath","//input[@id='LastName']").send_keys("S")
time.sleep(2)


driver.find_element("xpath","//input[@id='Email']").send_keys("son199m@gmail.com")
time.sleep(2)

driver.find_element("xpath","//input[@id='Password']").send_keys("Soumya")
time.sleep(2)

driver.find_element("xpath","//input[@id='ConfirmPassword']").send_keys("Soumya")
time.sleep(2)

driver.find_element("xpath","//input[@id='register-button']").click()
time.sleep(3)

driver.find_element("xpath","//input[@value='Continue']").click()
time.sleep(3)

driver.find_element("xpath","//a[@href='/logout']").click()
time.sleep(3)

driver.find_element("xpath","//a[@href='/login']").click()
time.sleep(3)

driver.find_element("xpath","//input[@id='Email']").send_keys("son199m@gmail.com")
time.sleep(2)

driver.find_element("xpath","//input[@id='Password']").send_keys("Soumya")
time.sleep(2)

driver.find_element("xpath","//input[@id='RememberMe']").click()


driver.find_element("xpath","//a[@href='/passwordrecovery']").click()

driver.find_element("xpath","//input[@id='Email']").send_keys("son199m@gmail.com")

time.sleep(2)
driver.find_element("xpath","//input[@name='send-email']").click()

#driver.find_element("xpath","//input[@class='button-1 login-button']").click()

