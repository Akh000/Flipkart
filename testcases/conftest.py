from selenium import webdriver
import pytest


def pytest_addoption(parser):
    return parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)

    driver.maximize_window()
    yield driver
    driver.close()
