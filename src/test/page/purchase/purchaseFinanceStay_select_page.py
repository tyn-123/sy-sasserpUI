from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class PurchaseFinanceStaySelectPage(Page):
    pay_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[4]/div/button/span')

    def purchasefinancestay_new_pay_button(self):
        time.sleep(1)
        pay_button_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.stay-receipt-bd > div.default-form-section.default-form-section-table > div:nth-child(1) > div.default-form-box > div > div.tabs-bd > div:nth-child(4) > div > button").scrollIntoView()'
        self.driver.execute_script(pay_button_js)
        time.sleep(1)
        self.find_element(*self.pay_button).click()
        time.sleep(1)

    