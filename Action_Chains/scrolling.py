'''

scroll_to_element()------>scroll till specified element
'''

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(2)
# #######--------------   using action_chains ------------------##
#
# # ref_ele=driver.find_element("xpath","//p[text()=' USEFUL LINKS ']")
# # ac_obj.scroll_to_element(ref_ele).perform()


#---------------------------------------------------------------------------------------------------#

''' -------------Using Java Script commands--------------------'''


'''         Using execute_script        '''
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# driver.execute_script("arguments[0].scrollIntoView();", ref_ele)


#################################################################################################################################


'''
scroll till end of the app---clicking end key from keyboard through automation
'''

# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(5)
#
# ac_obj.send_keys(Keys.HOME).perform()
# time.sleep(2)


##--------------------------------------------------------------------------------------
'''         Using execute_script        '''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
# ## To go back to the start of the application
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

# ###################################################################################################


'''
scroll using pg dn(page down)
'''

# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()

'''
OWN_combining page-up/down with HOME/END
'''
#
#
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(2)
#
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(5)
#
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.HOME).perform()



'''
scroll by pixels-----scroll_by_amount()
'''

#
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
#
# ac_obj.scroll_by_amount(0,1000).perform()

###----------Using Java Script---------------------------------------------------------#

# driver.execute_script("window.scrollBy(0, 1000);")       ## will scroll down by 500 pixels
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, -500);")      ## will scroll up by 500 pixels
###############################################################################################################################


