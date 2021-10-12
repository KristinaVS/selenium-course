import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    request.addfinalizer(browser.quit)
    return browser


def test_task13(driver):
    driver.get("http://localhost:801/litecart")
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    for i in range(3):
        driver.find_element_by_css_selector("#box-most-popular li").click()
        if len(driver.find_elements_by_css_selector(".buy_now select")) > 0:
            Select(driver.find_element_by_name("options[Size]")).select_by_value("Small")
        driver.find_element_by_name("add_cart_product").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i + 1)))
        driver.back()
    driver.find_element_by_css_selector("#cart a.link").click()
    count_row = len(driver.find_elements_by_css_selector("#order_confirmation-wrapper tr"))
    count_product = len(driver.find_elements_by_name("remove_cart_item"))
    for i in range(count_product):
        driver.find_element_by_name("remove_cart_item").click()
        if len(driver.find_elements_by_css_selector("#checkout-cart-wrapper em")) != 0:
            break
        wait.until(lambda d=webdriver:
                   len(d.find_elements_by_css_selector("#order_confirmation-wrapper tr")) == count_row - 1)
