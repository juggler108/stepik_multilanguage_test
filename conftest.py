from time import sleep
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose the language!")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"

    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get(link)
    sleep(10)
    yield driver

    print("\nquit browser..")
    driver.quit()
