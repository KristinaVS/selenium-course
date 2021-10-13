import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    request.addfinalizer(browser.quit)
    return browser


def test_task13(driver):
    driver.get("http://localhost:801/litecart/admin")
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']//span[text()='Catalog']").click()
    driver.find_element_by_css_selector(".dataTable .row:nth-child(3) td:nth-child(3) a").click()
    count = len(driver.find_elements_by_css_selector(".dataTable .row td:nth-child(3) a"))
    for i in range(count - 3):
        driver.find_element_by_css_selector(".dataTable .row:nth-child(" + str(i + 5) + ") td:nth-child(3) a").click()
        assert len(driver.get_log("browser")) == 0, "При открытии товара присутствуют сообщения в логе браузера!"
        driver.back()
