from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class PurchaseFinanceStayListPage(Page):
    PURCHASEFINANCESTAYLISTPAGE_LIST_URL = '/finance-stay-pay-list'
    pay_button = (By.XPATH,'//*[@class="ivu-btn ivu-btn-text ivu-btn-small"]/span')
    def purchasefinancestay_pay_button(self):
        time.sleep(1)
        self.find_element(*self.pay_button).click()
        time.sleep(1)
