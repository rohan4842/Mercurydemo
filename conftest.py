import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser", default = "chrome", action = "store", help ="enter name")
@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":

        PROXY = "localhost:1231"  # IP:PORT or HOST:PORT
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
        driver = webdriver.Chrome(chrome_options=chrome_options)

    elif browser == "Ie":
        driver = webdriver.Ie()

    driver.get("http://newtours.demoaut.com/mercurywelcome.php")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.quit()


