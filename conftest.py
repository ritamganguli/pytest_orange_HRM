#browser setup file

import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Specify the browser to use (e.g., Chrome, Firefox, etc.)")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(10)
        request.cls.driver=driver
        yield
        driver.close()

# @pytest.fixture(params=[{"firstName":"Ritam","lastName":"Ganguli","gender":"male"},{"firstName":"Pata Nahi","lastName":"Ganguli","gender":"male"}])
# def getData(request):
#     return request.param
    
