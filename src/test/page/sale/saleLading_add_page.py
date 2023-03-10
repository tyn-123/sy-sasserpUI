from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleLadingListAddPage(Page):
    tijiao_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[5]/button[2]/span')

    def sale_lading_new(self):
        time.sleep(1)
        self.find_element(*self.tijiao_button).click()
        time.sleep(1)