
from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.iforex.in/tools/live-rates ')
time.sleep(2)

driver.find_element("xpath","(//div[@id='ai-chat-bubble-close'])[2]").click()
time.sleep(6)

gold_sp=driver.find_element("xpath","(//div[text()='Gold']/../..//span)[2]")
gold_bp=driver.find_element("xpath","(//div[text()='Gold']/../..//span)[3]")

time.sleep(2)

print(f'The selling price of gold is {gold_sp.text}')
print(f'The selling price of gold is {gold_bp.text}')