from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SettingOrderListPage(Page):
    SETTINGORDERLISTPAGE_LIST_URL = '/setting-order-setting'
    baocun_button = (By.XPATH,'//*[@class="form-footer-item ivu-btn ivu-btn-primary"]/span')
    ladingSet_allow_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[9]/div/div[2]/div/label[1]')
    ladingSet_notallow_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[9]/div/div[2]/div/label[2]')  
    ladingDirectDeliverySet_true_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[12]/div/div[2]/div/label[1]/span/input')
    ladingDirectDeliverySet_false_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[12]/div/div[2]/div/label[2]/span/input')
    orderLadingOnlyOne_true_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[10]/div[1]/div[2]/div/label[1]/span')
    deliveryOutAutoSettlement_false_button =(By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[10]/div[2]/div/div/label[2]')

    def setting_order_baocun_button(self):
        time.sleep(1)
        self.find_element(*self.baocun_button).click()
        time.sleep(1)

    def setting_order_ladingSet_allow(self):
        """允许创建提货通知单"""
        time.sleep(1)
        self.find_element(*self.ladingSet_allow_button).click()
        time.sleep(1)

    def setting_order_ladingSet_notallow(self):
        """不允许创建提货通知单"""
        time.sleep(1)
        self.find_element(*self.ladingSet_notallow_button).click()
        time.sleep(1)

    def setting_order_ladingDirectDeliverySet_true(self):
        """提货通知单直接发货为是"""
        time.sleep(1)
        ladingDirectDeliverySet_dw_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div:nth-child(12) > div > div:nth-child(1) > span").scrollIntoView()'
        self.driver.execute_script(ladingDirectDeliverySet_dw_js)
        time.sleep(1)
        self.find_element(*self.ladingDirectDeliverySet_true_button).click()
        time.sleep(1)
        
    def setting_order_ladingDirectDeliverySet_false(self):
        """提货通知单直接发货为否"""
        time.sleep(1)
        ladingDirectDeliverySet_dw_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div:nth-child(12) > div > div:nth-child(1) > span").scrollIntoView()'
        self.driver.execute_script(ladingDirectDeliverySet_dw_js)
        time.sleep(1)
        self.find_element(*self.ladingDirectDeliverySet_false_button).click()
        time.sleep(1)

    def setting_order_orderLadingOnlyOne_true(self):
        """订单仅允许单次提货、发货为是"""
        time.sleep(1)
        self.find_element(*self.orderLadingOnlyOne_true_button).click()
        time.sleep(1)

    def setting_order_deliveryOutAutoSettlement_false(self):
        """发货后自动结算否"""
        time.sleep(1)
        self.find_element(*self.deliveryOutAutoSettlement_false_button).click()
        time.sleep(1)