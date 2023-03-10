from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleOrderListPage(Page):
    SALEORDERLISTPAGE_LIST_URL = '/sale-order-list'
    sale_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div/div[1]/button/span')
    take_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[28]/div/div/button[1]/span')

    def sale_order_new_button(self):
        time.sleep(1)
        self.find_element(*self.sale_button).click()
        time.sleep(1)

    def sale_order_take_button(self):
        time.sleep(1)
        self.find_element(*self.take_button).click()
        time.sleep(1)

