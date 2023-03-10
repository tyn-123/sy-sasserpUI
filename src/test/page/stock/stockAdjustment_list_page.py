from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class StockAdjustmentListPage(Page):
    STOCKADJUSTMENTLISTPAGE_LIST_PAGE_URL = '/stock-adjustment-list'
    stockadjustment_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/button/span/span')
    manualEntry_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/ul/li[2]')
    execute_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div[1]/div[2]/table/tbody/tr[1]/td[19]/div/div/button[1]/span')

    def stockadjustment_new_button(self):
        time.sleep(1)
        self.find_element(*self.stockadjustment_button).click()
        time.sleep(1)

    def manualEntry_new_button(self):
        time.sleep(1)
        self.find_element(*self.manualEntry_button).click()
        time.sleep(1)
    
    def stockadjustment_execute_button(self):
        time.sleep(1)
        self.find_element(*self.execute_button).click()
        time.sleep(1)