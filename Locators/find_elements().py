'''
WAP to print footer elements as a text using find_elements(),for loop

'''
from selenium.webdriver.common.by import By

'''
WAP to print all the colours in adidas shoes in myntra.com
'''






# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
#
# footer_elements=driver.find_elements("xpath","//div[@class='footer-menu-wrapper']//a")
#return type of find_elements = list of web elements
# '''
# here we are locating the web elements which has anchor tag(Each footer element has anchor tag in common.
# so we are extracting all occurrences using for loop)
# '''
# print(footer_elements)
#
# for ele in footer_elements:
#     print(ele.text)

###################################################################################################################################################

#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
#
# categories=driver.find_elements("xpath","//div[@class='block block-category-navigation']//a")
#
# for category in categories:
#
#     print(category.text)



'''
1.  wap to fetch all the popular searches from https://www.myntra.com/
2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''
'''
1.  wap to fetch all the popular searches from https://www.myntra.com/
'''
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
#
# search_links=driver.find_elements("xpath","//div[@class='desktop-pSearchlinks']//a")
#
# for link in search_links:
#     print(link.text)

#######################################################################################################################################################################

'''
2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
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
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
#
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
#
# driver.find_element("xpath","//span[contains(text(),'+')]").click()
#
# colors=driver.find_elements("xpath","//div[@class='vertical-filters-filters'][2]//label")
#
# for clrs in colors:
#     print(clrs.text)

####################################################################################################################################################

'''
3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
'''
#
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.zomato.com/Chennai')
# driver.maximize_window()
# time.sleep(2)
#
# delivery=driver.find_element("xpath","//input[@placeholder='Search for restaurant, cuisine or a dish']")
# delivery.send_keys("Pizza")
# delivery.click()
# time.sleep(2)
#
# dominos=driver.find_element("xpath","(//p[@class='sc-1hez2tp-0 sc-gFXMyG jkvifB'])[1]")
# dominos.click()
# time.sleep(2)
#
# driver.find_element("xpath",'''//h4[text()="Domino's Pizza"]''').click()
# time.sleep(2)
#
#
# pizza_list=driver.find_elements("xpath","//h4[@class='sc-fZEjqe jToeOs']")   #164
# pizza_price=driver.find_elements("xpath","//span[@class='sc-17hyc2s-1 cCiQWA']")   #164
#
# for pizza,price in zip(pizza_list,pizza_price):
#     print(pizza.text,"=",price.text)

###################################################################################################################################################
'''
4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.bookmyshow.com/')
#
# driver.find_element("xpath","//p[text()='Chennai']").click()
# driver.maximize_window()
# time.sleep(2)
#
#
# driver.find_element("xpath","//div[text()='See All ›']").click()
# time.sleep(2)
#
#
# movie_list=driver.find_elements("xpath","//div[@class='sc-7o7nez-0 elfplV']")
#
# for movie in movie_list:
#     time.sleep(2)
#     print(movie.text)

#did not print last 12 movies


########################################################################################################################################################################

'''
wap to enter data at a time in mulitple text boxes

'''


from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('file:///C:/Users/Naveen/Desktop/Soumya/demo.html')
time.sleep(2)

all_textboxes = driver.find_elements("xpath", '//input[@name="fname"]')













'''
wap to print all the links in python.org
'''
#
#
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# all_links=driver.find_elements("tag name", "a")
# for link in all_links:
#     print(link.get_attribute("href"))












