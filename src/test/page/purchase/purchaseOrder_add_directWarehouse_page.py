from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time
import datetime

class PurchaseOrderAddPage(Page):
    supplier_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/input')
    # supplier_xlk =(By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[3]/div/div/div/div[1]/div/div/div[2]/ul[2]')
    supplier_xlk =(By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[3]/div/div/div/div/div/div/div[2]/ul[2]/li/span')
    purchasedate_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[5]/div/div/div/div/div[1]/div/input')
    iswarehouse_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[13]/div/div/div/div/label[1]/span/input')
    detailsadd_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/button/span')
    putong_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]')
    putong_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]')
    pingmin_input = (By.XPATH,'/html/body/div[35]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/form/div/div[1]/div/div/div/div[1]/div/input')
    pingmin_xlk = (By.XPATH,'/html/body/div[35]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/form/div/div[1]/div/div/div/div[2]/ul[2]')
    select_button = (By.XPATH,'/html/body/div[35]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/button[2]/span')
    shangping1_xkk = (By.XPATH,'/html/body/div[35]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input')
    shangping2_xkk = (By.XPATH,'/html/body/div[35]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')
    quding_button = (By.XPATH,'/html/body/div[35]/div[2]/div/div/div[3]/div/div/button[2]/span')
    warehouse_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[9]/div/div/div/div/div/div/input')
    warehouse_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[9]/div/div/div/div/div/div/input')
    warehouse_xlk1 = (By.XPATH,'/html/body/div[40]/ul[2]/li[1]/span')
    warehouse_xlk2 = (By.XPATH,'/html/body/div[43]/ul[2]/li[1]/span')
    purchasePrice_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/div/div/div/div[2]/div[2]/input')
    purchasePrice_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[10]/div/div/div/div[2]/div[2]/input')
    purchaseAmount_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[11]/div/div/div/div[2]/div[2]/input')
    purchaseAmount_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[11]/div/div/div/div[2]/div[2]/input')
    purchaseWeight_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[12]/div/div/div/div[2]/div[2]/input')
    purchaseWeight_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[12]/div/div/div/div[2]/div[2]/input')
    inwarehouseAmount_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[13]/div/div/div/div[2]/div[2]/input')
    inwarehouseAmount_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[13]/div/div/div/div[2]/div[2]/input')
    inwarehouseWeight_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[14]/div/div/div/div[2]/div[2]/input')
    inwarehouseWeight_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[14]/div/div/div/div[2]/div[2]/input')
    baocun_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/button[2]/span')

    def purchase_order_new(self,gys,ck,dj,sl,zl,rksl,rkzl,pm):
        xiahua_js = "window.scrollTo(0, document.body.scrollHeight)" 
        time.sleep(1)
        self.find_element(*self.supplier_input).click()
        time.sleep(1)
        self.find_element(*self.supplier_input).send_keys(gys)
        time.sleep(1)
        self.find_element(*self.supplier_xlk).click()
        time.sleep(1)
        self.find_element(*self.purchasedate_input).send_keys("%s" %datetime.date.today())
        time.sleep(1)
        self.find_element(*self.iswarehouse_button).click()
        time.sleep(1)

        self.find_element(*self.detailsadd_button).click()
        time.sleep(1)
        self.find_element(*self.putong_button).click()
        time.sleep(1)
        self.find_element(*self.pingmin_input).click()
        time.sleep(1)
        self.find_element(*self.pingmin_input).send_keys(pm)
        time.sleep(1)
        self.find_element(*self.pingmin_xlk).click()
        time.sleep(1)
        self.find_element(*self.select_button).click()
        time.sleep(1)
        self.find_element(*self.shangping1_xkk).click()
        self.find_element(*self.shangping2_xkk).click()
        time.sleep(1)
        self.driver.execute_script(xiahua_js)
        self.find_element(*self.quding_button).click()
        time.sleep(2)

        warehouse_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(9) > div > div > div > div > div > div > input").scrollIntoView()'
        self.driver.execute_script(warehouse_dw1_js)
        self.find_element(*self.warehouse_input1).click()
        time.sleep(1)
        self.find_element(*self.warehouse_input1).send_keys(ck)
        time.sleep(1)
        self.find_element(*self.warehouse_xlk1).click()
        time.sleep(1)
        
        warehouse_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(9) > div > div > div > div > div > div > input").scrollIntoView()'    
        self.driver.execute_script(warehouse_dw2_js)
        time.sleep(1)
        self.find_element(*self.warehouse_input2).click()
        time.sleep(1)
        self.find_element(*self.warehouse_input2).send_keys(ck)
        time.sleep(1)
        self.find_element(*self.warehouse_xlk2).click()
        time.sleep(1)

        purchasePrice_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(10) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(purchasePrice_dw1_js)
        self.find_element(*self.purchasePrice_input1).send_keys(dj)
        time.sleep(1)
        purchaseAmount_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(purchaseAmount_dw1_js)
        self.find_element(*self.purchaseAmount_input1).send_keys(sl)
        time.sleep(1)
        purchaseWeight_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(12) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(purchaseWeight_dw1_js)
        self.find_element(*self.purchaseWeight_input1).send_keys(zl)
        time.sleep(1)
        inwarehouseAmount_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(13) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(inwarehouseAmount_dw1_js)
        self.find_element(*self.inwarehouseAmount_input1).send_keys(rksl)
        time.sleep(1)
        inwarehouseWeight_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(14) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(inwarehouseWeight_dw1_js)
        self.find_element(*self.inwarehouseWeight_input1).send_keys(rkzl)
        time.sleep(1)

        purchasePrice_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(10) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(purchasePrice_dw2_js)
        self.find_element(*self.purchasePrice_input2).send_keys(dj)
        time.sleep(1)
        purchaseAmount_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(11) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(purchaseAmount_dw2_js)
        self.find_element(*self.purchaseAmount_input2).send_keys(sl)
        time.sleep(1)
        purchaseWeight_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(12) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(purchaseWeight_dw2_js)
        self.find_element(*self.purchaseWeight_input2).send_keys(zl)
        time.sleep(1)
        inwarehouseAmount_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(13) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(inwarehouseAmount_dw2_js)
        self.find_element(*self.inwarehouseAmount_input2).send_keys(rksl)
        time.sleep(1)
        inwarehouseWeight_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table.form-expand-table-hide-overflow > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(14) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(inwarehouseWeight_dw2_js)
        self.find_element(*self.inwarehouseWeight_input2).send_keys(rkzl)
        time.sleep(1)
        
        self.find_element(*self.baocun_button).click()

        time.sleep(3)