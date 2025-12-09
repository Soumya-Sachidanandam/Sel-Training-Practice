#dependent/Independent x-path

#clicking on checkbox ruby even if the options are interchanged

#clicking on checkbox depends on the text associated to it

#same xpath should work for all positions of ruby

#Steps:
'''

    1.Identify the dependent and independent elements

    2.Write the x-path for the independent element

    3.Traverse back until you get the common match

    4.Continue writing the xpath for the dependent element

    To traverse back to the immediate parent use " /.. " until you get a common match and then stop

    Ex:python 3.14.0 release version link

    Ex:in.tradingview.com.click on search bar.in search bar type 'HAl: andclick in search icon and print the value of HAL which is dynamic

    Whenever the value is changing the
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://in.tradingview.com/')
time.sleep(2)

driver.find_element('xpath', '//span[text()="Search"]').click()
time.sleep(2)

driver.find_element('xpath', '//input[@name="query"]').send_keys('Tatamotors')
time.sleep(2)

driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
time.sleep(2)

tatamotors = driver.find_element('xpath', '//span[text()="TATAMOTORS"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
print(tatamotors.text)

