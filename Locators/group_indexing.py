import time
from selenium import webdriver
c_driver=webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

##############################################

# driver.get("https://blinkit.com/")
# time.sleep(3)
#
# driver.find_element("xpath","//button[text()='Detect my location']").click()

# driver.get("https://business.facebook.com/signup")
#
# time.sleep(3)
#
# driver.find_element("xpath","(//input[@type='text'])[1]").send_keys("soumya")

#################################


#try clicking on men, women,kids,etc by group indexing
#
# driver.get("https://myntra")
#
# time.sleep(3)
#
# driver.find_element("xpath","(//input[@type='text'])[1]").send_keys("soumya")

####################

#if the text contains unwanted spaces use contains()

#syntax: //tagname[contains(text(),"partial text")]

driver.get("https://www.giva.co/")