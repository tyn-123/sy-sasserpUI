from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time 

class StockAllocationAddPage(Page):
    callOutWarehouse_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[2]/div/div/div/div/div/div/input')
    callOutWarehouse_xlk = (By.XPATH,'/html/body/div[6]/ul[2]/li/span')
    callInWarehouse_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[4]/div/div/div/div/div/div/input')
    callInWarehouse_xlk = (By.XPATH,'/html/body/div[7]/ul[2]/li/span')
    businessDepartment_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[5]/div/div/div/div/div/div/input')
    businessDepartment_xlk = (By.XPATH,'/html/body/div[8]/ul[2]/li/span')
    businessUser_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[6]/div/div/div/div/div/div/input')
    businessUser_xlk = (By.XPATH,'/html/body/div[9]/ul[2]/li/span')
    detailsadd_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div/div[1]/div/div[1]/button/span')
    addWarehouse_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div/div[1]/div/div[2]/ul/li[2]')
    shangping1 = (By.XPATH,'/html/body/div[23]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input')
    shangping2 = (By.XPATH,'/html/body/div[23]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')
    quding_button = (By.XPATH,'/html/body/div[23]/div[2]/div/div/div[3]/div/div/button[2]/span')
    callOutAmount1_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/div/div/div/div[2]/div[2]/input')
    callOutWeight1_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[11]/div/div/div/div[2]/div[2]/input')
    callOutAmount2_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[10]/div/div/div/div[2]/div[2]/input')
    callOutWeight2_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[11]/div/div/div/div[2]/div[2]/input')
    tijiao_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[5]/button[2]/span')

    def stockallocation_new(self,callOutWarehouse,callInWarehouse,businessDepartment,businessUser,callOutAmount,callOutWeight):
        time.sleep(1)

        self.find_element(*self.callOutWarehouse_input).click()
        time.sleep(1)
        self.find_element(*self.callOutWarehouse_input).send_keys(callOutWarehouse)
        time.sleep(1)
        self.find_element(*self.callOutWarehouse_xlk).click()
        time.sleep(1)

        self.find_element(*self.callInWarehouse_input).click()
        time.sleep(1)
        self.find_element(*self.callInWarehouse_input).send_keys(callInWarehouse)
        time.sleep(1)
        self.find_element(*self.callInWarehouse_xlk).click()
        time.sleep(1)

        self.find_element(*self.businessDepartment_input).click()
        time.sleep(1)
        self.find_element(*self.businessDepartment_input).send_keys(businessDepartment)
        time.sleep(1)
        self.find_element(*self.businessDepartment_xlk).click()
        time.sleep(1)

        self.find_element(*self.businessUser_input).click()
        time.sleep(1)
        self.find_element(*self.businessUser_input).clear()
        self.find_element(*self.businessUser_input).send_keys(businessUser)
        time.sleep(1)
        self.find_element(*self.businessUser_xlk).click()
        time.sleep(1)

        self.find_element(*self.detailsadd_button).click()
        time.sleep(1)
        self.find_element(*self.addWarehouse_button).click()
        time.sleep(1)
        self.find_element(*self.shangping1).click()
        self.find_element(*self.shangping2).click()
        time.sleep(1)
        quding_js = 'document.querySelector("body > div:nth-child(26) > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > div > button.ivu-btn.ivu-btn-primary").scrollIntoView()'
        self.driver.execute_script(quding_js)
        self.find_element(*self.quding_button).click()
        time.sleep(1)

        callOutAmount1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1 > div.has-btn-view > div:nth-child(3) > div.default-form-box > div > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(10) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(callOutAmount1_js)
        time.sleep(1)
        self.find_element(*self.callOutAmount1_input).clear()
        time.sleep(1)
        self.find_element(*self.callOutAmount1_input).send_keys(callOutAmount)
        time.sleep(1)
        self.find_element(*self.callOutWeight1_input).clear()
        time.sleep(1)
        self.find_element(*self.callOutWeight1_input).send_keys(callOutWeight)
        time.sleep(1)

        callOutAmount2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1 > div.has-btn-view > div:nth-child(3) > div.default-form-box > div > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(10) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default").scrollIntoView()'
        self.driver.execute_script(callOutAmount2_js)
        time.sleep(1)
        self.find_element(*self.callOutAmount2_input).clear()
        time.sleep(1)
        self.find_element(*self.callOutAmount2_input).send_keys(callOutAmount)
        time.sleep(1)
        self.find_element(*self.callOutWeight2_input).clear()
        time.sleep(1)
        self.find_element(*self.callOutWeight2_input).send_keys(callOutWeight)
        time.sleep(1)

        self.find_element(*self.tijiao_button).click()
        time.sleep(1)




        