from selenium.webdriver.common.by import By
from src.test.common.page import Page
import time

class SaleOrderAddPage(Page):
    customer_input = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[3]/div/div/div/div/div/div/div[1]/div/input')
    customer_xlk = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[3]/div/div/div/div[1]/div/div/div[2]/ul[2]/li/span')
    kjck_ture_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[1]/form/div/div[12]/div/div/div/div/label[1]/span/input')
    detailsadd_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[1]/button[1]/span')
    shangping1_fxk = (By.XPATH,'/html/body/div[17]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input')
    shangping2_fxk = (By.XPATH,'/html/body/div[17]/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div[4]/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')
    quding_button = (By.XPATH,'/html/body/div[17]/div[2]/div/div/div[3]/button/span')
    saleAmount_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[9]/div/div/div/div[2]/div[2]/input')
    saleAmount_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[9]/div/div/div/div[2]/div[2]/input')
    saleWeight_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/div/div/div/div[2]/div[2]/input')
    saleWeight_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[10]/div/div/div/div[2]/div[2]/input')
    salePrice_input1 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[1]/td[11]/div/div/div/div[2]/div[2]/input')
    salePrice_input2 = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[11]/div/div/div/div[2]/div[2]/input')
    baocun_button = (By.XPATH,'/html/body/div[1]/main/article/div/div[2]/div[1]/div[4]/button[2]/span')

    def sale_order_new(self,kh,sl,zl,dj):
        time.sleep(1)
        self.find_element(*self.customer_input).click()
        time.sleep(1)
        self.find_element(*self.customer_input).send_keys(kh)
        time.sleep(1)
        self.find_element(*self.customer_xlk).click()
        time.sleep(1)

        self.find_element(*self.kjck_ture_button).click()
        time.sleep(1)

        detailsadd_button_dw_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.form-box-handle > button.box-handle-item.ivu-btn.ivu-btn-primary.ivu-btn-ghost > span").scrollIntoView()'
        self.driver.execute_script(detailsadd_button_dw_js)
        time.sleep(1)
        self.find_element(*self.detailsadd_button).click()
        time.sleep(1)
        self.find_element(*self.shangping1_fxk).click()
        self.find_element(*self.shangping2_fxk).click()
        time.sleep(2)
        quding_button_dw_js = 'document.querySelector("body > div:nth-child(20) > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > button > span").scrollIntoView()'
        self.driver.execute_script(quding_button_dw_js)
        time.sleep(1)
        self.find_element(*self.quding_button).click()
        time.sleep(1)

        saleAmount_input_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(9) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(saleAmount_input_dw1_js)
        self.find_element(*self.saleAmount_input1).clear()
        self.find_element(*self.saleAmount_input1).send_keys(sl)
        time.sleep(1)

        saleWeight_input_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(10) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(saleWeight_input_dw1_js)
        self.find_element(*self.saleWeight_input1).clear()
        self.find_element(*self.saleWeight_input1).send_keys(zl)
        time.sleep(1)

        salePrice_input_dw1_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(salePrice_input_dw1_js)
        self.find_element(*self.salePrice_input1).send_keys(dj)
        time.sleep(1)

        saleAmount_input_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(9) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(saleAmount_input_dw2_js)
        self.find_element(*self.saleAmount_input2).clear()
        self.find_element(*self.saleAmount_input2).send_keys(sl)
        time.sleep(1)

        saleWeight_input_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(10) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(saleWeight_input_dw2_js)
        self.find_element(*self.saleWeight_input2).clear()
        self.find_element(*self.saleWeight_input2).send_keys(zl)
        time.sleep(1)

        salePrice_input_dw2_js = 'document.querySelector("body > div.h-100 > main > article > div > div.content-view.bg-grey.flex-1.is-fixed-btn > div:nth-child(1) > div.default-form-section.default-form-section-table > div.default-form-box > div.editable-table.form-expand-table > div.table-box > div > div.ivu-table.ivu-table-small.ivu-table-border > div.ivu-table-body.ivu-table-overflowX > table > tbody > tr:nth-child(2) > td:nth-child(11) > div > div > div > div.input-number.ivu-input-number.ivu-input-number-default > div.ivu-input-number-input-wrap > input").scrollIntoView()'
        self.driver.execute_script(salePrice_input_dw2_js)
        self.find_element(*self.salePrice_input2).send_keys(dj)
        time.sleep(1)

        self.find_element(*self.baocun_button).click()
        time.sleep(1)
        


