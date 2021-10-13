from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from task19.pages.main_page import MainPage
from task19.pages.product_page import ProductPage
from task19.pages.basket_page import BasketPage


class Application:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)
        self.main_page = MainPage(self.browser)
        self.product_page = ProductPage(self.browser)
        self.basket_page = BasketPage(self.browser)

    def open(self):
        self.main_page.open()
        self.main_page.max_window()

    def quit(self):
        self.browser.quit()

    def add_product_in_basket(self):
        for i in range(3):
            self.main_page.go_to_product_page()
            self.product_page.product_in_basket()
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i + 1)))
            self.product_page.go_back()

    def go_to_basket(self):
        self.main_page.go_to_basket_page()

    def delete_product_in_basket(self):
        count_row = self.basket_page.get_tables_row()
        count_product = self.basket_page.get_product_in_basket()
        for i in range(count_product):
            self.basket_page.stop_products_carousel()
            self.basket_page.delete_product()
            if self.basket_page.check_empty_basket():
                break
            self.wait.until(lambda d=self.browser:
                            len(d.find_elements_by_css_selector("#order_confirmation-wrapper tr")) == count_row - 1)
