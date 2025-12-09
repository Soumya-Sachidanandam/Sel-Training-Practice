import time

## EG1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

ac = ActionChains(driver)

driver.get('https://www.linkedin.com')
time.sleep(2)

# driver.find_element('xpath','//span[text()="Continue with Google"]').click()
# time.sleep(2)


#Locating the iframe

google_frame=driver.find_element('xpath','//iframe[@title="Sign in with Google Button"]').click()
time.sleep(2)

#switching to iframe
driver.switch_to.frame(google_frame)

#Performing op on iframe
driver.find_element('xpath','//span[text()="Continue with Google"]').click()

#Switch to parent
driver.switch_to.parent_frame()


#Perform op on parent
ref_ele=driver.find_element('xpath','//h2[@id="bottom-cta-section__header"]')
ac.move_to_element(ref_ele)
time.sleep(2)



