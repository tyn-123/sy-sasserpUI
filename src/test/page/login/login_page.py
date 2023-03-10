from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time


class LoginPage(Page):
    user_input = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/form/div[1]/div/div/div/div[1]/div/input')
    password_input = (By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[2]/form/div[2]/div/div/div/div[1]/div/input')
    # xieyi_checkbox = (By.CLASS_NAME,'ivu-checkbox-inner')
    login_button = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/button')
    def login(self, ui ,pi):
        """登录"""
        time.sleep(3)
        self.find_element(*self.user_input).send_keys(ui)      
        self.find_element(*self.password_input).send_keys(pi)
        # self.find_element(*self.xieyi_checkbox).click()
        self.find_element(*self.login_button).click()
        time.sleep(2)

# LoginPage.login('XF','Asdf@1234')