import time
from BaseClass import BaseClass
from adminpannel import AdminBoard
from buzzpage import BuzzPage
from dashboard import Dashboard
from loginpage import LoginPage



class TestCase(BaseClass):
    
    def test_title(self):
        log=self.getLogger()
        login_page = LoginPage(self.driver)
        dashboard=Dashboard(self.driver)
        buzz_page=BuzzPage(self.driver)
        log.info("The title of the page is: "+login_page.get_title())
        login_page.enter_user_pass()
        log.info("Entered User Name Password")
        if "dashboard" in login_page.get_current_url():
            print("Sucesfully Logged In")
            log.info("Sucesfully Logged In")
        else:
            print("Failed to log in")
            log.warn("Didnt log")
        if "Punched Out:" in (dashboard.verify_punch()):
            print("Verified Punch Out")
            log.info("Punched Out....")
        action_item=(dashboard.verify_action_items())
        for i in action_item:
            print(i)
            log.info(i+" Is There in action item")
        print("The Sidebar Items Is")
        sidebar_items=dashboard.items_in_sidebar()
        for i in sidebar_items:
            print(i)
            log.info(i+" Is There in sidebar")
        admin_board=AdminBoard(self.driver)
        admin_board.go_to_admin()
        admin_board.select_job_roles()
        #admin_board.select_job_titles()
        print(admin_board.select_job_titles())
        log.info("Sucuesffuly verified that job titles is working")
        admin_board.check_job_tiles_delete()
        admin_board.check_job_tiles_delete_confirm_delete()
        admin_board.verify_if_can_edit_job_titles()
        admin_board.select_more()
        log.info("Selected More")
        admin_board.select_email_subscription()
        log.info("Selected Email Subscription")
        dashboard.scroll_in_sidebar("//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']/parent::a/parent::li/parent::ul/li[12]")
        log.info("Going to Buzz Page...")
        buzz_page.check_sharable()
        