from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleSettlementAddPage(Page):
    customer_input = (By.XPATH,'//*[@class="ivu-modal-body"]/div[2]/div/div[1]/form/div/div[2]/div/div/div/div/div/div/input')
    customer_xlk = (By.XPATH,'/html/body/div[20]/ul[2]/li/span')
    search_button = (By.XPATH,'/html/body/div[27]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/button[3]/span')
    mx1_xkk = (By.XPATH,'//*[@class="ivu-modal-body"]/div[3]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input')
    mx2_xkk = (By.XPATH,'//*[@class="ivu-modal-body"]/div[3]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')
    # quding1_button = (By.XPATH,'/html/body/div[27]/div[2]/div/div/div[3]/button[2]/span')
    qudiing2_button = (By.XPATH,'//*[@class="ivu-modal-confirm-footer"]/button[2]/span')
    back_button = (By.XPATH,'//*[@class="ivu-modal-confirm-footer"]/button[1]/span')

    def  location_quding_button(self):
        """定位确定按钮,确定按钮的层级总是变化，无法获取固定的路径"""
        for i in range(25,35):
            self.quding_button = (By.XPATH,'/html/body/div['+str(i)+']/div[2]/div/div/div[3]/button[2]/span')
            try:
                self.find_element(*self.quding_button).click()
                break
            except:
                continue

    def sale_settlement_new(self,kh):
        time.sleep(20)
        self.find_element(*self.customer_input).click()
        time.sleep(1)
        self.find_element(*self.customer_input).send_keys(kh)
        time.sleep(1)
        self.find_element(*self.customer_xlk).click()
        time.sleep(1)
        self.find_element(*self.search_button).click()
        time.sleep(1)
        self.find_element(*self.mx1_xkk).click()
        self.find_element(*self.mx2_xkk).click()
        time.sleep(1)
        quding1_button_dw_js = 'document.querySelector("body > div:nth-child(30) > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > button.ivu-btn.ivu-btn-primary > span").scrollIntoView()'
        self.driver.execute_script(quding1_button_dw_js)
        time.sleep(1)
        self.location_quding_button()
        # self.find_element(*self.quding1_button).click()
        time.sleep(1)
        self.find_element(*self.qudiing2_button).click()
        time.sleep(1)
        self.find_element(*self.back_button).click()
        time.sleep(60)