from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class PurchaseOrderListPage(Page):
    PURCHASEORDERPAGE_LIST_URL = '/purchase-order-list'

    purchase_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div/div[1]/button')
    receipt_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[28]/div/div/button[1]/span')
    def purchase_order_new_button(self):
        time.sleep(1)
        self.find_element(*self.purchase_button).click()
        time.sleep(1)

    def purchase_order_receipt_button(self):
        time.sleep(1)
        self.find_element(*self.receipt_button).click()
        time.sleep(1)

    