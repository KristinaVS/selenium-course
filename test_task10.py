import ast
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver_chrome(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    request.addfinalizer(browser.quit)
    return browser


@pytest.fixture
def driver_firefox(request):
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    request.addfinalizer(browser.quit)
    return browser


@pytest.fixture
def driver_ie(request):
    browser = webdriver.Ie(capabilities={"requireWindowFocus": True})
    browser.implicitly_wait(3)
    request.addfinalizer(browser.quit)
    return browser


def test_task10_1(driver_chrome):
    driver_chrome.get("http://localhost:801/litecart")
    driver_chrome.maximize_window()
    product = driver_chrome.find_element_by_css_selector("#box-campaigns li")
    product_name = product.find_element_by_css_selector(".name").text
    product_price = product.find_element_by_css_selector(".regular-price").text
    product_price_color = product.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    product_price_tag = product.find_element_by_css_selector(".regular-price").tag_name
    product_price_size = product.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    product_sale = product.find_element_by_css_selector(".campaign-price").text
    product_sale_color = product.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    product_sale_tag = product.find_element_by_css_selector(".campaign-price").tag_name
    product_sale_size = product.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    product.click()
    name = driver_chrome.find_element_by_css_selector("h1.title").text
    price = driver_chrome.find_element_by_css_selector(".regular-price").text
    price_color = driver_chrome.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    price_tag = driver_chrome.find_element_by_css_selector(".regular-price").tag_name
    price_size = driver_chrome.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    sale = driver_chrome.find_element_by_css_selector(".campaign-price").text
    sale_color = driver_chrome.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    sale_tag = driver_chrome.find_element_by_css_selector(".campaign-price").tag_name
    sale_size = driver_chrome.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert product_name == name, "Неверное название! В карточке: " + product_name + ". На странице: " + name
    assert product_price == price, "Неверная обычная цена! В карточке: " + product_price + ". На странице: " + price
    assert product_sale == sale, "Неверная цена со скидкой! В карточке: " + product_sale + ". На странице: " + sale
    assert product_price_tag == "s", "Обычная цена в карточке не зачеркнута! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(product_price_color.strip("rgba"))
    assert r == g == b, "Неверный цвет обычной цены в карточке!"
    assert price_tag == "s", "Обычная цена на странице продукта не зачеркнута! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(price_color.strip("rgba"))
    assert r == g == b, "Неверный цвет обычной цены на странице!"
    assert product_sale_tag == "strong", "Акционная цена в карточке не жирная! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(product_sale_color.strip("rgba"))
    assert (g == 0) and (b == 0), "Неверный цвет акционной цены в карточке!"
    assert sale_tag == "strong", "Акционная цена на странице продукта не жирная! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(sale_color.strip("rgba"))
    assert (g == 0) and (b == 0), "Неверный цвет акционной цены на странице!"
    assert product_price_size.split('px')[0] < product_sale_size.split('px')[0], \
        "Акционная цена в карточке меньше, чем обычная!"
    assert price_size.split('px')[0] < sale_size.split('px')[0], \
        "Акционная цена на странице продукта меньше, чем обычная!"


def test_task10_2(driver_firefox):
    driver_firefox.get("http://localhost:801/litecart")
    driver_firefox.maximize_window()
    product = driver_firefox.find_element_by_css_selector("#box-campaigns li")
    product_name = product.find_element_by_css_selector(".name").text
    product_price = product.find_element_by_css_selector(".regular-price").text
    product_price_color = product.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    product_price_tag = product.find_element_by_css_selector(".regular-price").tag_name
    product_price_size = product.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    product_sale = product.find_element_by_css_selector(".campaign-price").text
    product_sale_color = product.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    product_sale_tag = product.find_element_by_css_selector(".campaign-price").tag_name
    product_sale_size = product.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    product.click()
    name = driver_firefox.find_element_by_css_selector("h1.title").text
    price = driver_firefox.find_element_by_css_selector(".regular-price").text
    price_color = driver_firefox.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    price_tag = driver_firefox.find_element_by_css_selector(".regular-price").tag_name
    price_size = driver_firefox.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    sale = driver_firefox.find_element_by_css_selector(".campaign-price").text
    sale_color = driver_firefox.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    sale_tag = driver_firefox.find_element_by_css_selector(".campaign-price").tag_name
    sale_size = driver_firefox.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert product_name == name, "Неверное название! В карточке: " + product_name + ". На странице: " + name
    assert product_price == price, "Неверная обычная цена! В карточке: " + product_price + ". На странице: " + price
    assert product_sale == sale, "Неверная цена со скидкой! В карточке: " + product_sale + ". На странице: " + sale
    assert product_price_tag == "s", "Обычная цена в карточке не зачеркнута! (Имеет неверный тэг)"
    r, g, b = ast.literal_eval(product_price_color.strip("rgba"))
    assert r == g == b, "Неверный цвет обычной цены в карточке!"
    assert price_tag == "s", "Обычная цена на странице продукта не зачеркнута! (Имеет неверный тэг)"
    r, g, b = ast.literal_eval(price_color.strip("rgba"))
    assert r == g == b, "Неверный цвет обычной цены на странице!"
    assert product_sale_tag == "strong", "Акционная цена в карточке не жирная! (Имеет неверный тэг)"
    r, g, b = ast.literal_eval(product_sale_color.strip("rgba"))
    assert (g == 0) and (b == 0), "Неверный цвет акционной цены в карточке!"
    assert sale_tag == "strong", "Акционная цена на странице продукта не жирная! (Имеет неверный тэг)"
    r, g, b = ast.literal_eval(sale_color.strip("rgba"))
    assert (g == 0) and (b == 0), "Неверный цвет акционной цены на странице!"
    assert product_price_size.split('px')[0] < product_sale_size.split('px')[0], \
        "Акционная цена в карточке меньше, чем обычная!"
    assert price_size.split('px')[0] < sale_size.split('px')[0], \
        "Акционная цена на странице продукта меньше, чем обычная!"


def test_task10_3(driver_ie):
    driver_ie.get("http://localhost:801/litecart")
    driver_ie.maximize_window()
    product = driver_ie.find_element_by_css_selector("#box-campaigns li")
    product_name = product.find_element_by_css_selector(".name").text
    product_price = product.find_element_by_css_selector(".regular-price").text
    product_price_color = product.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    product_price_tag = product.find_element_by_css_selector(".regular-price").tag_name
    product_price_size = product.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    product_sale = product.find_element_by_css_selector(".campaign-price").text
    product_sale_color = product.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    product_sale_tag = product.find_element_by_css_selector(".campaign-price").tag_name
    product_sale_size = product.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    product.click()
    name = driver_ie.find_element_by_css_selector("h1.title").text
    price = driver_ie.find_element_by_css_selector(".regular-price").text
    price_color = driver_ie.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    price_tag = driver_ie.find_element_by_css_selector(".regular-price").tag_name
    price_size = driver_ie.find_element_by_css_selector(".regular-price").value_of_css_property("font-size")
    sale = driver_ie.find_element_by_css_selector(".campaign-price").text
    sale_color = driver_ie.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    sale_tag = driver_ie.find_element_by_css_selector(".campaign-price").tag_name
    sale_size = driver_ie.find_element_by_css_selector(".campaign-price").value_of_css_property("font-size")
    assert product_name == name, "Неверное название! В карточке: " + product_name + ". На странице: " + name
    assert product_price == price, "Неверная обычная цена! В карточке: " + product_price + ". На странице: " + price
    assert product_sale == sale, "Неверная цена со скидкой! В карточке: " + product_sale + ". На странице: " + sale
    assert product_price_tag == "s", "Обычная цена в карточке не зачеркнута! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(product_price_color.strip("rgba"))
    assert r == g == b, "Неверный цвет обычной цены в карточке!"
    assert price_tag == "s", "Обычная цена на странице продукта не зачеркнута! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(price_color.strip("rgba"))
    assert r == g == b, "Неверный цвет обычной цены на странице!"
    assert product_sale_tag == "strong", "Акционная цена в карточке не жирная! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(product_sale_color.strip("rgba"))
    assert (g == 0) and (b == 0), "Неверный цвет акционной цены в карточке!"
    assert sale_tag == "strong", "Акционная цена на странице продукта не жирная! (Имеет неверный тэг)"
    r, g, b, a = ast.literal_eval(sale_color.strip("rgba"))
    assert (g == 0) and (b == 0), "Неверный цвет акционной цены на странице!"
    assert float(product_price_size.split('px')[0]) < float(product_sale_size.split('px')[0]), \
        "Акционная цена в карточке меньше, чем обычная!"
    assert float(price_size.split('px')[0]) < float(sale_size.split('px')[0]), \
        "Акционная цена на странице продукта меньше, чем обычная!"
