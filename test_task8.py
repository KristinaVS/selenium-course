import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    request.addfinalizer(browser.quit)
    return browser


def test_task8(driver):
    driver.get("http://localhost:801/litecart")
    driver.maximize_window()
    product_list = driver.find_elements_by_css_selector("div.content .products li")
    for product in product_list:
        sticker = product.find_elements_by_css_selector(".sticker")
        count = len(sticker)
        assert count == 1, "Неверное количество стикеров. Должен быть 1. Отображается " + str(count)
