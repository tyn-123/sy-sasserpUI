from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class PurchaseSettlementListPage(Page):
    PURCHASESETTLEMENTPAGE_LIST_URL = '/purchase-settlement-list'
    settlement_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div/div[1]/button[1]/span')
    send_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[21]/div/div/button[2]/span')

    def purchase_settlement_new_button(self):
        time.sleep(1)
        self.find_element(*self.settlement_button).click()
        time.sleep(1)

    def purchase_settlement_send_button(self):
        time.sleep(1)
        self.find_element(*self.send_button).click()
        time.sleep(1)
