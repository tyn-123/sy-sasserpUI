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
from src.test.page.settingOrder.settingOrder_list_page import SettingOrderListPage
from src.test.page.sale.saleOrder_list_page import SaleOrderListPage
from src.test.page.sale.saleOrder_add_ztsf_page import SaleOrderAddPage
from src.test.page.sale.saleLading_list_page import SaleLadingListPage
from src.test.page.sale.saleLading_add_page import SaleLadingListAddPage
from src.test.page.sale.saleSettlement_list_page import SaleSettlementListPage
from src.test.page.sale.saleSettlement_add_page import SaleSettlementAddPage
from src.test.page.sale.saleStayReceipt_list_page import SaleStayReceiptListPage
from src.test.page.sale.saleStayReceipt_select_page import SaleStayReceiptSelectPage
from src.test.page.sale.saleStayReceipt_add_page import SaleStayReceiptAddPage

class TestSale(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_sale.xlsx'

    def sub_setUp(self):
        self.page = LoginPage().get(self.URL,open = True)

    def test_saleOrder(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])

                self.page = SettingOrderListPage(self.page)
                self.page.get(self.URL + SettingOrderListPage().SETTINGORDERLISTPAGE_LIST_URL)
                time.sleep(1)
                self.page.setting_order_ladingDirectDeliverySet_false()
                time.sleep(1)
                self.page.setting_order_deliveryOutAutoSettlement_false()
                time.sleep(1)
                self.page.setting_order_baocun_button()
                time.sleep(1)


                self.page = SaleOrderListPage(self.page)
                self.page.get(self.URL + SaleOrderListPage().SALEORDERLISTPAGE_LIST_URL)
                time.sleep(1)
                self.page.sale_order_new_button()
                time.sleep(1)     

                self.page.handle_switch()
                self.page = SaleOrderAddPage(self.page)
                self.page.sale_order_new(d['customer'],d['saleAmount'],d['saleWeight'],d['salePrice'])
                time.sleep(1)

                self.page = SaleLadingListPage(self.page)
                self.page.get(self.URL + SaleLadingListPage().SALELADINGLISTPAGE_LIST_URL)
                time.sleep(1)
                self.page.sale_lading_new_button()
                time.sleep(1)

                self.page.handle_switch()
                self.page = SaleLadingListAddPage(self.page)
                time.sleep(1)
                self.page.sale_lading_new()
                time.sleep(1)

                self.page.handle_switch(0)
                self.page = SaleSettlementListPage(self.page)
                self.page.get(self.URL + SaleSettlementListPage().SALESETTLEMENTLISTPAGE_LIST_URL)
                time.sleep(1)
                self.page.sale_settlement_new_button()
                time.sleep(1)

                self.page = SaleSettlementAddPage(self.page)
                time.sleep(1)
                self.page.sale_settlement_new(d['customer'])
                time.sleep(1)

                self.page = SaleSettlementListPage(self.page)
                time.sleep(1)
                self.page.sale_settlement_send_button()
                time.sleep(1)

                self.page = SaleStayReceiptListPage(self.page)
                self.page.get(self.URL + SaleStayReceiptListPage.SALESTAYRECEIPTLISTPAGE_LIST_PAGE)
                time.sleep(1)
                self.page.sale_stayreceipt_new_button()
                time.sleep(1)

                self.page.handle_switch()
                self.page = SaleStayReceiptSelectPage(self.page)
                time.sleep(1)
                self.page.sale_stayreceipt_new_receipt_button()
                time.sleep(1)

                self.page.handle_switch()
                self.page = SaleStayReceiptAddPage(self.page)
                time.sleep(1)
                self.page.sale_stayreceipt_new(d['receiptPrice'])
                time.sleep(10)

    def sub_tearDown(self):
        self.page.quit()

if __name__ == '__main__':
    report  = REPORT_PATH + '\\test_sale_zitishoufa.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(TestSale('test_saleOrder'))
