from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleStayReceiptSelectPage(Page):
    receipt_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/button/span')

    def sale_stayreceipt_new_receipt_button(self):
        time.sleep(1)
        receipt_button_dw_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div:nth-child(2) > div.default-form-section.default-form-section-table > div:nth-child(1) > div.default-form-box > div > div.tabs-bd > div > div > button > span").scrollIntoView()'
        self.driver.execute_script(receipt_button_dw_js)
        time.sleep(1)
        self.find_element(*self.receipt_button).click()
        time.sleep(1)
