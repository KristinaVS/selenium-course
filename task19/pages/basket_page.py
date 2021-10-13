class BasketPage:
    def __init__(self, browser, timeout=2):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def get_tables_row(self):
        return len(self.browser.find_elements_by_css_selector("#order_confirmation-wrapper tr"))

    def get_product_in_basket(self):
        return len(self.browser.find_elements_by_name("remove_cart_item"))

    def stop_products_carousel(self):
        count_shortlist_product = self.browser.find_elements_by_css_selector(".shortcuts>.shortcut>a")
        if len(count_shortlist_product) > 0:
            count_shortlist_product[0].click()

    def delete_product(self):
        self.browser.find_element_by_name("remove_cart_item").click()

    def check_empty_basket(self):
        if len(self.browser.find_elements_by_css_selector("#checkout-cart-wrapper em")) != 0:
            return True
        else:
            return False
