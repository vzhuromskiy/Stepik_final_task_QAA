import pytest
from selenium import webdriver
import time


#  создаем фикстуру
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()

#  Встроенная фикстура request позволяет получать данные
#  о текущем запущенном тесте, что позволяет, например,
#  сохранять дополнительные данные в отчёт, а также делать
#  многие другие интересные вещи.
#  Настраивать тестовые окружения с помощью передачи параметров
#  через командную строку можно с помощью встроенной функции pytest_addoption
#  и фикстуры request.
#  Для запроса значения параметра мы можем вызвать команду:
#  browser_name = request.config.getoption("browser_name")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
