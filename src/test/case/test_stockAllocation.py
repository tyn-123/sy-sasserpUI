import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append("./")
from src.utils.config import Config, DRIVER_PATH,DATA_PATH,REPORT_PATH
from src.utils.log import logger
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner
from src.test.page.login.login_page import LoginPage
from src.test.page.stock.stockAllocation_list_page import StockAllocationListPage
from src.test.page.stock.stockAllocation_add_page import StockAllocationAddPage
from src.test.page.stock.stockAllocation_edit_page import StockAllocationEditPage

class TestStockAllocation(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_stockAllocation.xlsx'

    def sub_setUp(self):
        self.page = LoginPage().get(self.URL,open=True)
    
    def test_stockallocation(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])

                self.page = StockAllocationListPage(self.page)
                self.page.get(self.URL + StockAllocationListPage().STOCKALLOCTIONLISTPAGE_LISTr_URL)
                time.sleep(1)
                self.page.stockallocation_new_button()
                time.sleep(1)

                self.page.handle_switch()
                self.page = StockAllocationAddPage(self.page)
                time.sleep(1)
                self.page.stockallocation_new(d['callOutWarehouse'],d['callInWarehouse'],d['businessDepartment'],d['businessUser'],d['callOutAmount'],d['callOutWeight'])
                time.sleep(1)

                self.page.handle_switch(0)
                self.page = StockAllocationListPage(self.page)
                self.page.get(self.URL + StockAllocationListPage().STOCKALLOCTIONLISTPAGE_LISTr_URL)
                time.sleep(1)
                self.page.stockallocation_execute_button()
                time.sleep(1)

                self.page.handle_switch()
                self.page = StockAllocationEditPage(self.page)
                time.sleep(1)
                self.page.stockallocation_execute()
                time.sleep(1)

    def sub_tearDown(self):
        self.page.quit()


if __name__ == '__main__':
    report = REPORT_PATH + '\\test_stockallocation.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='自动化测试报告',description='测试用例执行情况:')
        runner.run(TestStockAllocation('test_stockallocation'))