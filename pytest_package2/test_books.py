import time

class TestBooks:
    def test_click_book(self,setup):
        setup.find_element('xpath', '(//a[contains(text(),"Books")])[3]').click()
        time.sleep(1)
    def test_add_cart(self,setup):
        setup.find_element('xpath', '(//input[@value="Add to cart"])[1]').click()