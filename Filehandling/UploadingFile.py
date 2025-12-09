'''
uploading single file
'''

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/ ')
driver.maximize_window()
time.sleep(2)


file1=r"C:\Users\Naveen\Desktop\DBNotes.txt"
driver.find_element("xpath","//input[@id='singleFileInput']").send_keys(f'{file1}')








###################################################################################################################################
'''
uploading multiple files
'''


from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/ ')
driver.maximize_window()
time.sleep(2)



file1=r"C:\Users\Naveen\PycharmProjects\Selenium_Training\training\Files\myntra.png"
file2=r"C:\Users\Naveen\PycharmProjects\Selenium_Training\training\Files\myntra1.png"

driver.find_element("xpath","//input[@id='multipleFilesInput']").send_keys(f'{file1}\n{file2}')