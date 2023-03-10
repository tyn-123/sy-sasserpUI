from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time 

class PurchaseSettlemnentAddPage(Page):
    supplierName_input  = (By.XPATH,'//*[@class="ivu-modal-content"]/div[2]/div[2]/div/div[1]/form/div/div[2]/div/div/div/div/div/div/input')
    supplierName_xlk = (By.XPATH,'//*[@class="ivu-select-dropdown ivu-select-dropdown-transfer"]/ul[2]/li[1]')
    search_button = (By.XPATH,'//*[@class="ivu-modal-content"]/div[2]/div[2]/div/div[2]/div/button[3]/span')
    mx1_xkk = (By.XPATH,'//*[@class="ivu-modal-content"]/div[2]/div[3]/div[1]/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input')
    mx2_xkk = (By.XPATH,'//*[@class="ivu-modal-content"]/div[2]/div[3]/div[1]/div/div[1]/div[5]/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')
    # quding_button = (By.XPATH,'/html/body/div[29]/div[2]/div/div/div[3]/button[2]/span')
    quding2_button = (By.XPATH,'//*[@class="ivu-modal-confirm-footer"]/button[2]/span')
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

    def purchase_settlemnent_new(self,gs):
        # xiahua_js = "window.scrollTo(0, document.body.scrollHeight)" 
        time.sleep(1)
        self.find_element(*self.supplierName_input).click()
        time.sleep(1)
        self.find_element(*self.supplierName_input).send_keys(gs)
        time.sleep(1)
        self.find_element(*self.supplierName_xlk).click()
        time.sleep(1)
        self.find_element(*self.search_button).click()
        time.sleep(1)
        self.find_element(*self.mx1_xkk).click()
        self.find_element(*self.mx2_xkk).click()
        time.sleep(1)
        quding_button_dw_js = 'document.querySelector("body > div:nth-child(32) > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > button.ivu-btn.ivu-btn-primary > span").scrollIntoView()'
        # 执行JS代码（driver.execute_script(“js语句“)）
        self.driver.execute_script(quding_button_dw_js)
        self.location_quding_button()
        # self.find_element(*self.quding_button).click()
        time.sleep(1)
        self.find_element(*self.quding2_button).click()
        time.sleep(1)
        self.find_element(*self.back_button).click()
        time.sleep(1)


# try:
#     self.find_element(*self.supplierName_input)
#     supplierName_input = 
# except:
#     self.find_element(*self.supplierName_input)
#     supplierName_input = 


