import time
from selenium.webdriver.support.ui import Select


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        title = self.driver.title
        print("Page title:", title)
        return title


    def enter_user_pass(self):
        self.driver.find_element_by_css_selector("input[name='username']").send_keys("Admin")
        time.sleep(5)
        self.driver.find_element_by_css_selector("input[name='password']").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(10)
        
    def get_current_url(self):
        url=self.driver.current_url
        return url
    