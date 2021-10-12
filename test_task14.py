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


def test_task14(driver):
    driver.get("http://localhost:801/litecart/admin")
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']//span[text()='Countries']").click()
    driver.find_element_by_css_selector("#content a.button").click()
    count_ref = driver.find_elements_by_css_selector("table table a[target]")
    for ref in count_ref:
        current_window = driver.current_window_handle
        list_window = driver.window_handles
        ref.click()
        wait.until(EC.new_window_is_opened(list_window))
        new_list_window = driver.window_handles
        new_list_window.remove(current_window)
        if len(new_list_window) > 0:
            driver.switch_to.window(new_list_window[0])
            driver.close()
            driver.switch_to.window(current_window)
