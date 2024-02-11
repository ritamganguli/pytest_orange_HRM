import time
from selenium.webdriver.support.ui import Select


class AdminBoard:
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin(self):
        time.sleep(100)
        self.driver.find_element_by_xpath("//span[text()='Admin']").click()
        time.sleep(10)
    def select_job_roles(self):
        self.driver.find_element_by_xpath("//li[@class='oxd-topbar-body-nav-tab']/parent::ul/li[2]").click()
        time.sleep(10)
    def select_job_titles(self):
        self.driver.find_element_by_xpath("//li[@class='oxd-topbar-body-nav-tab']/parent::ul/li[2]/ul/li[1]/a").click()
        time.sleep(10)
        job_titles=self.driver.find_element_by_xpath("//div[@class='orangehrm-header-container']/h6").text
        return job_titles
        
    def check_job_tiles_delete(self):
        self.driver.find_element_by_xpath("//button[@class='oxd-icon-button oxd-table-cell-action-space']/parent::div/button[1]").click()
        time.sleep(10)
    def check_job_tiles_delete_confirm_delete(self):
        self.driver.find_element_by_xpath("//div[@class='orangehrm-modal-footer']/button[2]").click()
        time.sleep(10)
    def verify_if_can_edit_job_titles(self):
        self.driver.find_element_by_xpath("//div[@class='oxd-table-cell-actions']/button[2]").click()
        time.sleep(10)
    def select_more(self):
        self.driver.find_element_by_xpath("//li[@class='oxd-topbar-body-nav-tab']/parent::ul/li[7]").click()
        time.sleep(10)
    def select_email_subscription(self):
        self.driver.find_element_by_xpath("//a[text()='Email Subscriptions']").click()
        time.sleep(10)
        
    


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
    
    