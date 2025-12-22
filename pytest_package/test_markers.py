import pytest

#
# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

###############################################################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")

###############################################################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")


##############################################################################################################################

#
# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

#############################################################################################################################
# @pytest.mark.sanity
# class TestSample:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.regression
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

################################################################################################################################
#
# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#
# @pytest.mark.regression
# class TestExample:
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")


######################################################################################################################################
#
# @pytest.mark.skip
# def test_login():
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout executing")

######################################################################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip(reason="reg already done")
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.skip(reason="signup already done")
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

######################################################################################################################################


# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

######################################################################################################################################

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

def test_login():
    driver.find_element("id", "user-name").send_keys('standard_user')
    time.sleep(1)
    driver.find_element('id', 'password').send_keys('secret_sauce')
    time.sleep(1)
    driver.find_element('id', 'login-button').click()
    time.sleep(3)

def test_logout():
    if 'inventory' not in driver.current_url:
        pytest.skip("login is unsuccessful")

    driver.find_element('id', 'react-burger-menu-btn').click()
    time.sleep(2)
    driver.find_element('id', 'logout_sidebar_link').click()







































