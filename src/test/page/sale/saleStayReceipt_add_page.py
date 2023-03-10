from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time
import datetime

class SaleStayReceiptAddPage(Page):
    now = str(datetime.datetime.now())[:4]+str(datetime.datetime.now())[5:7]+str(datetime.datetime.now())[8:10]+str(datetime.datetime.now())[11:13]+str(datetime.datetime.now())[14:16]
    receiptDate_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/div[2]/form/div/div[6]/div/div/div/div[1]/div/input')
    paymentFlow_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/form/div/div[3]/div/div/div[1]/input')
    receiptPrice_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/form[1]/div/div[1]/div/div/div[1]/div[2]/div[2]/input')
    tijiao_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[5]/button[2]/span')

    def sale_stayreceipt_new(self,je):
        time.sleep(1)
        self.find_element(*self.receiptDate_input).send_keys("%s" %datetime.date.today())
        time.sleep(1)
        paymentFlow_input_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div:nth-child(2) > div.default-form-box > form > div > div:nth-child(3) > div > div > div.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text > input").scrollIntoView()'
        self.driver.execute_script(paymentFlow_input_js)
        time.sleep(1)
        self.find_element(*self.paymentFlow_input).send_keys(self.now)
        time.sleep(1)
        self.find_element(*self.receiptPrice_input).send_keys(je)
        time.sleep(1)
        self.find_element(*self.tijiao_input).click()
        time.sleep(1)
