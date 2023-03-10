from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleStayReceiptListPage(Page):
    SALESTAYRECEIPTLISTPAGE_LIST_PAGE = '/finance-stay-receipt-list'
    receipt_button = (By.XPATH,'//*[@class="ivu-btn ivu-btn-text ivu-btn-small"]/span')
    def sale_stayreceipt_new_button(self):
        time.sleep(1)
        self.find_element(*self.receipt_button).click()
        time.sleep(1)
