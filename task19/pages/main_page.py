class MainPage:
    def __init__(self, browser, timeout=2):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get("http://localhost:801/litecart")

    def max_window(self):
        self.browser.maximize_window()

    def go_to_product_page(self):
        self.browser.find_element_by_css_selector("#box-most-popular li").click()

    def go_to_basket_page(self):
        self.browser.find_element_by_css_selector("#cart a.link").click()
