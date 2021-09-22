import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    request.addfinalizer(browser.quit)
    return browser


def test_task7(driver):
    driver.get("http://localhost:801/litecart/admin")
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    tab_list = driver.find_elements_by_css_selector("#app->a")
    count_tab = len(tab_list)
    for number in range(count_tab):
        tab = driver.find_element_by_css_selector("#app-:nth-child(" + str(number + 1) + ")>a")
        driver.execute_script("arguments[0].scrollIntoView()", tab)
        tab.click()
        subtab_list = driver.find_elements_by_css_selector("#app-:nth-child(" + str(number + 1) + ") li")
        count_subtab = len(subtab_list)
        for number_subtab in range(count_subtab):
            subtab = driver.find_element_by_css_selector("#app-:nth-child(" + str(number + 1) + ") li:nth-child("
                                                         + str(number_subtab + 1) + ")")
            driver.execute_script("arguments[0].scrollIntoView()", subtab)
            subtab.click()
            assert driver.find_element_by_css_selector("#content h1"), "Заголовка страницы не найдено!"


def test_task8(driver):
    driver.get("http://localhost:801/litecart")
    driver.maximize_window()
    product_list = driver.find_elements_by_css_selector(".product.column.shadow.hover-light")
    for product in product_list:
        sticker = product.find_elements_by_css_selector(".sticker")
        count = len(sticker)
        assert count == 1, "Неверное количество стикеров. Должен быть 1. Отображается " + str(count)
