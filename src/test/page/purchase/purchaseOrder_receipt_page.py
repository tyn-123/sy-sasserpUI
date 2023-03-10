from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class PurchaseOrderReceiptPage(Page):
    baocun_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/button[2]/span')

    def purchase_order_receipt_button(self):
        time.sleep(2)
        self.find_element(*self.baocun_button).click()
        time.sleep(1)
