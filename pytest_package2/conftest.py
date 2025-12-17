# from selenium import webdriver
# import pytest
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.implicitly_wait(10)
#     driver.get('https://demowebshop.tricentis.com/')
#     driver.maximize_window()
#     time.sleep(2)
#     yield driver
#     driver.close()

############################################################################################################################################

import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action='store',
        default="chrome",
        help="Browser to run tests : chrome/firefox/edge"
    )

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.get('https://demowebshop.tricentis.com/')
    driver.maximize_window()

    # ac_obj = ActionChains(setup)
    # ref_ele=setup.find_element("xpath",'//input[@id="newsletter-subscribe-button"]')
    # ac_obj.scroll_to_element(ref_ele).perform()
    time.sleep(2)
    yield driver
    driver.close()