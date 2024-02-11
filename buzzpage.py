import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BuzzPage:
    def __init__(self, driver):
        self.driver = driver
        
    def check_sharable(self):
        time.sleep(70)
        self.driver.find_element_by_xpath("//div[@class='orangehrm-buzz-post-footer']/div/button[2]").click()
        time.sleep(20)
    