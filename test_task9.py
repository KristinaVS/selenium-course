import time

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    request.addfinalizer(browser.quit)
    return browser


def test_task9_1(driver):
    driver.get("http://localhost:801/litecart/admin/?app=countries&doc=countries")
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    country_list = driver.find_elements_by_css_selector("tr.row")
    country_name_list = []
    country_zone = []
    for country in country_list:
        country_name = country.find_element_by_css_selector("td:nth-child(5)").get_attribute("textContent")
        country_name_list.append(country_name)
        count_zone = country.find_element_by_css_selector("td:nth-child(6)").get_attribute("textContent")
        if str(count_zone) != "0":
            country_zone.append(country_name)
    country_sort = country_name_list
    country_sort.sort()
    assert country_name_list == country_sort, "Значения стран расположено не в алфавитном порядке!"
    for zone in country_zone:
        countries = driver.find_elements_by_css_selector("tr.row")
        for country in countries:
            value = country.find_element_by_css_selector("td:nth-child(5)").get_attribute("textContent")
            if zone == value:
                country.find_element_by_css_selector("td:nth-child(5)>a").click()
                zone_name_list = []
                zone_list = driver.find_elements_by_css_selector("#table-zones tr>td:nth-child(3)")
                for name in zone_list:
                    zone_name = name.get_attribute("textContent")
                    zone_name_list.append(zone_name)
                zone_name_sort = zone_name_list
                zone_name_sort.sort()
                assert zone_name_sort == zone_name_list, "Значения зон не отсортированы!"
                driver.back()
                break


def test_task9_2(driver):
    driver.get("http://localhost:801/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.maximize_window()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    country_list = driver.find_elements_by_css_selector("tr.row")
    count_country = len(country_list)
    for country in range(count_country):
        zone_name_list = []
        driver.find_element_by_xpath("//tr[@class='row'][" + str(country + 1) + "]/td[3]/a").click()
        zone_list = driver.find_elements_by_css_selector("tr>td:nth-child(3)>select option")
        for zone in zone_list:
            if zone.is_selected():
                zone_name_list.append(zone.get_attribute("textContent"))
        zone_sort = zone_name_list
        zone_sort.sort()
        assert zone_sort == zone_name_list, "Список зон не отсортирован!"
        driver.back()
