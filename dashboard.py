import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Dashboard:
    def __init__(self, driver):
        self.driver = driver
    def verify_punch(self):
        title = self.driver.find_element_by_xpath("//p[text()='Punched In']/parent::div/p[2]").text
        return title


    def verify_action_items(self):
        action_items=self.driver.find_elements_by_xpath("//div[@class='orangehrm-todo-list-item']/p")
        list1=[]
        for items in action_items:
            list1.append(items.text)
        return list1
    def items_in_sidebar(self):
        sidebar_items=self.driver.find_elements_by_xpath("//li[@class='oxd-main-menu-item-wrapper']/a/span")
        list2=[]
        for items in sidebar_items:
            list2.append(items.text)
        return list2
    def scroll_in_sidebar(self,item_scroll):
        div_element = self.driver.find_element_by_xpath(item_scroll)
        div_height = div_element.size['height']
        scrolls_needed = div_height // 100
        actions = ActionChains(self.driver)
        actions.move_to_element(div_element)
        for _ in range(scrolls_needed):
            actions.click_and_hold().move_by_offset(0, 100).perform()
        time.sleep(40)
        self.driver.find_element_by_xpath(item_scroll).click()
        time.sleep(30)
        screen_height = self.driver.execute_script("return window.innerHeight;")
        scroll_distance = int(screen_height *1.9)
        self.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(30)
        
        
        

    def enter_username_password(self):
        self.driver.find_element_by_id("txt-username").send_keys("John Doe")
        time.sleep(5)
        self.driver.find_element_by_id("txt-password").send_keys("ThisIsNotAPassword")
        time.sleep(5)

    def click_login(self):
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(10)
    def get_current_url(self):
        url=self.driver.current_url
        return url
    def select_dropdown_option(self):
        dropdown = Select(self.driver.find_element_by_id("combo_facility"))
        dropdown.select_by_index(2)
        time.sleep(5)
    def select_checkbox(self):
        self.driver.find_element_by_id("chk_hospotal_readmission").click()
        time.sleep(10)
    def select_date(self):
        self.driver.find_element_by_id("txt_visit_date").send_keys("04/02/2024")
        time.sleep(5)
        self.driver.find_element_by_id("txt_visit_date").click()
        time.sleep(10)
    def add_comment(self):
        self.driver.find_element_by_id("txt_comment").send_keys("Kuch Bhi...")
        time.sleep(10)
    def book_appointment_button(self):
        scroll_position = (60 / 100) * self.driver.execute_script("return document.body.scrollHeight;")
        self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(5)
        self.driver.find_element_by_id("btn-book-appointment").click()
        time.sleep(10)
    def booking_conformation(self):
        book_confirm=self.driver.find_element_by_xpath("//p[@class='lead']").text
        return book_confirm
        
    
    
