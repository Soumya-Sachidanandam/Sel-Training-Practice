'''
WAP to select August 2026 15 from makemytrip.com.

here we are making use of try block for exception handling. Because there is only 2 months displayed

so until we get august the while loop runs. Once it is met,the loop breaks

if in case the month is not august instead of throwing error we are handling it using except block by clicking

on the forward arrow

'''

#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')
# time.sleep(2)
#
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath","//span[@class='commonModal__close']").click()
# time.sleep(2)
#
# driver.find_element("xpath","//span[text()='Departure']").click()
# time.sleep(2)
#
# def select_date(month,date):
#     while True:
#
#         try:
#             driver.find_element("xpath",f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#
#         except:
#             driver.find_element("xpath","//span[@class='DayPicker-NavButton DayPicker-NavButton--next']").click()
#             time.sleep(2)
#
#
# select_date("January 2026",15)




################################################################################################################################################


'''
WAP to to select travel date in irctc website https://www.irctc.co.in/nget/train-search
'''



from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
time.sleep(2)

driver.find_element("xpath","//button[text()='OK']").click()
time.sleep(2)
driver.find_element("xpath","(//input[@type='text'])[3]").click()


def select_date_irctc(month,date):

    while True:

        try:

            #driver.find_element("xpath",'f//div[@class="ui-datepicker-title ng-tns-c69-9"]/../..//span[text()="{date}"]').click()
            #driver.find_element("xpath",f"//span[contains(text(),'{month}')]/../../..//span[contains(text(),'{date}')]").click()
            driver.find_element("xpath","(//span[text()='August']/../../..//span[@class='ui-state-default ui-state-disabled ng-tns-c69-9 ng-star-inserted'])[21]").click()
            break
        except:

            driver.find_element("xpath","//span[contains(@class,'ui-datepicker-next-icon')]").click()
            #time.sleep(2)

select_date_irctc("August",15)


##############################################################################################################################################
'''
WAP  to select travel date in https://www.booking.com/

'''
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.booking.com/')
# driver.maximize_window()
# time.sleep(2)












