def test_task19(driver):
    driver.open()
    driver.add_product_in_basket()
    driver.go_to_basket()
    driver.delete_product_in_basket()
