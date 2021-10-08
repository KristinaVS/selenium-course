import datetime
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


def test_task11(driver):
    driver.get("http://localhost:801/litecart/en/")
    driver.maximize_window()
    driver.find_element_by_css_selector("form>table a").click()
    driver.find_element_by_name("tax_id").send_keys(21)
    driver.find_element_by_name("company").send_keys("New")
    driver.find_element_by_name("firstname").send_keys("Kristina")
    driver.find_element_by_name("lastname").send_keys("Smoliakova")
    driver.find_element_by_name("address1").send_keys("address1")
    driver.find_element_by_name("address2").send_keys("address2")
    driver.find_element_by_name("postcode").send_keys(52382)
    driver.find_element_by_name("city").send_keys("City")
    select_country = Select(driver.find_element_by_name("country_code"))
    select_country.select_by_value("US")
    select_zone = Select(driver.find_element_by_css_selector("select[name=zone_code]"))
    select_zone.select_by_value("AS")
    now = datetime.datetime.now()
    email = "new" + now.strftime('%d%H%M%S') + "@mail.ru"
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("phone").send_keys(111111111)
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("confirmed_password").send_keys("admin")
    driver.find_element_by_name("create_account").click()
    driver.find_element_by_xpath("//div[@id='box-account']//a[text()='Logout']").click()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//div[@id='box-account']//a[text()='Logout']").click()
