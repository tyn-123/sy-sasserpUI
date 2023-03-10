from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time
import datetime

class PurchaseFinanceStayAddPage(Page):
    paydate_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div[2]/form/div/div[5]/div/div/div/div[1]/div/input')
    payprice_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/div[1]/div/div/div[1]/div[2]/div[2]/input')
    tijiao_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[5]/button[2]')

    def purchasefinancestay_new(self,je):
        time.sleep(1)
        self.find_element(*self.paydate_input).send_keys("%s" %datetime.date.today())
        time.sleep(1)
        payprice_input_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div:nth-child(3) > div.default-form-box > form:nth-child(2) > div > div.box-title-form > div > div > div.global-input-number-wrap.ivu-input-wrapper > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(payprice_input_js)
        time.sleep(1)
        self.find_element(*self.payprice_input).send_keys(je)
        time.sleep(1)
        self.find_element(*self.tijiao_button).click()
        time.sleep(1)



    