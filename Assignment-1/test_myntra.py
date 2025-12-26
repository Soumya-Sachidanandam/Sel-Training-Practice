import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)


@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    ac_obj = ActionChains(driver)
    driver.get('https://www.myntra.com/')
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()


class TestMyntra(object):
    def test_search(self,setup):
        setup.find_element('xpath','//input[@placeholder="Search for products, brands and more"]').send_keys("adidas")
        time.sleep(2)
        setup.find_element('xpath','//span[@class="myntraweb-sprite desktop-iconSearch sprites-search"]').click()
        time.sleep(2)

    def test_select(self,setup):
        setup.find_element('xpath','(//img[@class="img-responsive"])[3]').click()
        time.sleep(4)

    def test_select_size(self,setup):
        setup.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
        time.sleep(2)

        alert_obj = setup.switch_to.alert
        alert_obj.dismiss()
        time.sleep(2)

        setup.find_element("xpath","//p[contains(text(),'3')][1]").click()
        time.sleep(2)
