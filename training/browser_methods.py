import time
from selenium import webdriver

#opening chrome browser
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
f_driver=webdriver.Chrome(opts)

driver=webdriver.Chrome(opts)



#launching myntra
driver.get("https://www.myntra.com/")
time.sleep(3)

#maximize window
driver.maximize_window()
time.sleep(3)

#to get the title of the web app window
print(driver.title)
time.sleep(3)

#gives the name of the browser
print(driver.name)
time.sleep(3)

#goes back
driver.back()
time.sleep(3)

#goes forward
driver.forward()
time.sleep(3)

#gives the page source
print(driver.page_source)
time.sleep(3)

#minimize the window
driver.minimize_window()
time.sleep(3)

#To take screenshot
driver.save_screenshot("myntra_homepage.png")

#to save screenshot in a particular path.Here we created files directory->right click->copy path/ref click on first path and paste it
driver.save_screenshot(r'C:\Users\Naveen\PycharmProjects\Selenium_Training\training\Files\myntra1.png')

#to close the browser
driver.close()