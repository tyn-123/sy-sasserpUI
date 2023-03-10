from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleLadingListPage(Page):
    SALELADINGLISTPAGE_LIST_URL = '/sale-take-list'
    fahuo_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[2]/table/tbody/tr[1]/td[27]/div/div/button[1]/span')

    def sale_lading_new_button(self):
        time.sleep(1)
        self.find_element(*self.fahuo_button).click()
        time.sleep(1)