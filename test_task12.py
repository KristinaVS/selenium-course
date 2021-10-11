import datetime
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    request.addfinalizer(browser.quit)
    return browser


def test_task12(driver):
    driver.get("http://localhost:801/litecart/admin")
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']//span[text()='Catalog']").click()
    driver.find_element_by_xpath("//a[contains(text(), 'Add New Product')]").click()
    driver.find_element_by_xpath("//ul[@class='index']//a[text()='General']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//label[contains(text(), 'Enabled')]").click()
    driver.find_element_by_name("name[en]").send_keys("Name")
    driver.find_element_by_name("code").send_keys(11111111)
    driver.find_element_by_css_selector("input[data-name='Rubber Ducks']").click()
    driver.find_element_by_css_selector("input[value='1-1']").click()
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys(12)
    driver.find_element_by_name("new_images[]").send_keys(os.getcwd() + "\\picture.jpg")
    driver.find_element_by_css_selector("input[name=date_valid_from]").send_keys("01.10.2021")
    driver.find_element_by_css_selector("input[name=date_valid_to]").send_keys("30.10.2021")
    driver.find_element_by_xpath("//ul[@class='index']//a[text()='Information']").click()
    time.sleep(1)
    Select(driver.find_element_by_name("manufacturer_id")).select_by_value("1")
    driver.find_element_by_name("keywords").send_keys("new")
    driver.find_element_by_name("short_description[en]").send_keys("short description")
    driver.find_element_by_name("description[en]").send_keys("description")
    driver.find_element_by_name("head_title[en]").send_keys("title")
    driver.find_element_by_name("meta_description[en]").send_keys("meta")
    driver.find_element_by_xpath("//ul[@class='index']//a[text()='Prices']").click()
    time.sleep(1)
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys("23")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_value("USD")
    driver.find_element_by_name("gross_prices[USD]").clear()
    driver.find_element_by_name("gross_prices[USD]").send_keys("23")
    driver.find_element_by_name("gross_prices[EUR]").clear()
    driver.find_element_by_name("gross_prices[EUR]").send_keys("35")
    driver.find_element_by_name("save").click()
    time.sleep(1)
    catalog = driver.find_elements_by_css_selector(".dataTable .row>td:nth-child(3) a")
    flag = False
    for c in catalog:
        if "Name" == c.text:
            flag = True
    assert flag, "Созданного элемента не найдено в каталоге!"
