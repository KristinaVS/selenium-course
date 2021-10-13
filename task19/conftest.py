import pytest
from task19.app.application import Application
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    app = Application(driver)
    request.addfinalizer(app.quit)
    return app
