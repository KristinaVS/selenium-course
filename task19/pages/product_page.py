from selenium.webdriver.support.select import Select


class ProductPage:
    def __init__(self, browser, timeout=2):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def go_back(self):
        self.browser.back()

    def product_in_basket(self):
        if len(self.browser.find_elements_by_css_selector(".buy_now select")) > 0:
            Select(self.browser.find_element_by_name("options[Size]")).select_by_value("Small")
        self.browser.find_element_by_name("add_cart_product").click()
