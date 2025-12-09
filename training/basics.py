
from selenium import webdriver

#to launch chrome browser,Chrome browser closes automatically so by using opts=webdriver.ChromeOptions(),opts.add_experimental_option("detach", True) we are preventing it

c_driver=webdriver.Chrome()
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
f_driver=webdriver.Chrome(opts)


#to launch firefox browser
#webdriver=webdriver.Firefox()

#******No need to use opts.add_experimental_option("detach", True) because firfeox doesnot close automatically


#to launch Edge browser

opts=webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
e_driver=webdriver.Edge(opts)






