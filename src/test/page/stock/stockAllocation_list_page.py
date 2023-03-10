from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time 

class StockAllocationListPage(Page):
    STOCKALLOCTIONLISTPAGE_LISTr_URL = '/stock-allocation-list'
    stockallcoation_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div/div[1]/button/span')
    execute_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[15]/div/div/button[1]/span')

    def stockallocation_new_button(self):
        time.sleep(1)
        self.find_element(*self.stockallcoation_button).click()
        time.sleep(1)

    def stockallocation_execute_button(self):
        time.sleep(1)
        self.find_element(*self.execute_button).click()
        time.sleep(1)