import os
import sys 
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.log import logger
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.purchase.purchaseOrder_list_page import PurchaseOrderListPage
from src.test.page.purchase.purchaseOrder_add_page import PurchaseOrderAddPage
from src.test.page.purchase.purchaseOrder_receipt_page import PurchaseOrderReceiptPage
from src.test.page.purchase.purchaseSettlement_list_page import PurchaseSettlementListPage
from src.test.page.purchase.purchaseSettlement_add_page import PurchaseSettlemnentAddPage
from src.test.page.purchase.purchaseFinanceStay_list_page import PurchaseFinanceStayListPage
from src.test.page.purchase.purchaseFinanceStay_select_page import PurchaseFinanceStaySelectPage
from src.test.page.purchase.purchaseFinanceStay_add_page import PurchaseFinanceStayAddPage


class TestPurchase(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_purchase.xlsx'

    def sub_setUp(self):

        self.page = LoginPage().get(self.URL,open = True)

    def test_purchaseOrder(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])

                self.page = PurchaseOrderListPage(self.page)
                self.page.get(self.URL + PurchaseOrderListPage().PURCHASEORDERPAGE_LIST_URL)
                time.sleep(1)
                self.page.purchase_order_new_button()
                self.page.handle_switch()
                time.sleep(1)

                self.page = PurchaseOrderAddPage(self.page)
                time.sleep(1)
                self.page.purchase_order_new(d['supplier'],d['warehouse'],d['purchasePrice'],d['purchaseAmount'],d['purchaseWeight'],d['PingMin'])
                time.sleep(1)

                self.page = PurchaseOrderListPage(self.page)
                self.page.get(self.URL + PurchaseOrderListPage().PURCHASEORDERPAGE_LIST_URL)
                time.sleep(1)
                self.page.purchase_order_receipt_button()
                self.page.handle_switch()
                time.sleep(1)

                self.page = PurchaseOrderReceiptPage(self.page)
                time.sleep(1)
                self.page.purchase_order_receipt_button()
                time.sleep(1)
                
                self.page.handle_switch(0)
                self.page = PurchaseSettlementListPage(self.page)
                self.page.get(self.URL + PurchaseSettlementListPage().PURCHASESETTLEMENTPAGE_LIST_URL)
                time.sleep(1)
                self.page.purchase_settlement_new_button()
                time.sleep(1)

                self.page = PurchaseSettlemnentAddPage(self.page)
                self.page.purchase_settlemnent_new(d['supplier'])
                time.sleep(1)

                self.page = PurchaseSettlementListPage(self.page)
                time.sleep(1)
                self.page.purchase_settlement_send_button()
                time.sleep(1)

                self.page = PurchaseFinanceStayListPage(self.page)
                self.page.get(self.URL + PurchaseFinanceStayListPage().PURCHASEFINANCESTAYLISTPAGE_LIST_URL)
                time.sleep(1)
                self.page.purchasefinancestay_pay_button()
                self.page.handle_switch()
                time.sleep(1)

                
                self.page = PurchaseFinanceStaySelectPage(self.page)
                time.sleep(1)
                self.page.purchasefinancestay_new_pay_button()
                self.page.handle_switch()
                time.sleep(1)

                self.page = PurchaseFinanceStayAddPage(self.page)
                time.sleep(1)
                self.page.purchasefinancestay_new(d['payPrice'])
                time.sleep(2)


    def sub_tearDown(self):
        self.page.quit() 

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_purchase.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='用例执行情况:')
        runner.run(TestPurchase('test_purchaseOrder'))

        