import sys
import unittest
import time
sys.path.append('./')
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.file_reader import ExcelReader
from src.utils.log import logger
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.stock.stockAdjustment_list_page import StockAdjustmentListPage
from src.test.page.stock.stockAdjustment_add_page import StockAdjustmentAddPage

class TestStockAdjustment(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_stockadjustment_Price.xlsx'

    def sub_setUp(self):
        self.page =LoginPage().get(self.URL,open=True)
    
    def test_stockadjustment(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(datas=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])

                self.page = StockAdjustmentListPage(self.page)
                self.page.get(self.URL + StockAdjustmentListPage().STOCKADJUSTMENTLISTPAGE_LIST_PAGE_URL)
                time.sleep(1)
                self.page.stockadjustment_new_button()
                self.page.manualEntry_new_button()
                time.sleep(1)

                self.page.handle_switch()
                self.page = StockAdjustmentAddPage(self.page)
                time.sleep(1)
                self.page.stockAdjustment_LocationNumber(d['adjustmentType'],d['warehouse'],d['businessDepartment'],d['businessUser'])
                time.sleep(1)

                self.page = StockAdjustmentListPage(self.page)
                self.page.get(self.URL + StockAdjustmentListPage().STOCKADJUSTMENTLISTPAGE_LIST_PAGE_URL)
                time.sleep(1)
                self.page.stockadjustment_execute_button()
                time.sleep(1)

    def sub_tearDown(self):
        self.page.quit()

if __name__ in '__main__':
    report = REPORT_PATH + '\\test_stockadjustment_Price.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(TestStockAdjustment('test_stockadjustment'))
