import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])
def setup(request):
    parameter = request.param


    if parameter == 'chrome':
        driver=webdriver.Chrome()
    elif parameter == 'firefox':
        driver=webdriver.Firefox()
    elif parameter == 'edge':
        driver=webdriver.Edge()

    driver.implicitly_wait(5)
    driver.get('https://demowebshop.tricentis.com/')
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome()

class TestRegister:

    def test_reg_link(self, setup):     ## setup --> webdriver.Chrome()
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(1)
        ac_obj = ActionChains(setup)
        ref_ele=setup.find_element("xpath",'//input[@id="newsletter-subscribe-button"]')
        ac_obj.scroll_to_element(ref_ele).perform()
        time.sleep(1)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-female').click()
        time.sleep(2)

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('soumya')
        time.sleep(1)

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('s')
        time.sleep(1)

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('s123@gmail.com')
        time.sleep(1)

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('s@12345')
        time.sleep(1)

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('s@12345')

        time.sleep(1)

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('s123@gmail.com')
        time.sleep(1)

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('s@12345')