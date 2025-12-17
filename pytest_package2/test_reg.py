import time
from selenium.webdriver.common.action_chains import ActionChains
class TestRegister:

    def test_reg_link(self, setup):     ## setup --> webdriver.Chrome()
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)
        ac_obj = ActionChains(setup)
        ref_ele=setup.find_element("xpath",'//input[@id="newsletter-subscribe-button"]')
        ac_obj.scroll_to_element(ref_ele).perform()
        time.sleep(2)

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-female').click()
        time.sleep(2)

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('soumya')
        time.sleep(2)

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('s')
        time.sleep(2)

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('s123@gmail.com')
        time.sleep(2)

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('s@12345')
        time.sleep(2)

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('s@12345')

        time.sleep(2)
