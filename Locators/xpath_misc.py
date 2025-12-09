'''

get_attribute()
.text
get_attribute("outerHTML")
get_attribute("innerHTML")
get_dom_attribute("attributename")
assert keyword
webelement.tagname-->a property--gives the tagname Ex: women.tagname gives a as output which is a tag name
webelement.aria_role-->gives the role of the web element women.araia_role gives link as output
screenshot of a web element--locate the web element ---web element.screenshot("screenshotname.png")--If u don mention any location it

screenshot of enter page--driver.savescreenshot()
'''


'''
own example for assert
seat=4
book=int(input("Enter the no of seats"))
seat=seat-book
assert seat>=0,f'only {seat} seats are remaining'
i=1
while i<=book:

    name=input("Enter name")
    i=i+1
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)


driver.get("https://demowebshop.tricentis.com/register")

