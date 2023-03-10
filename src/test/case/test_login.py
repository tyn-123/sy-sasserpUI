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

class TestPurchase(unittest.TestCase):
    
    URL = Config().get('URL')
    excel = DATA_PATH + '/test_login.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = LoginPage().get(self.URL,open = True)

    def sub_tearDown(self):
        self.page.quit()

    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.login(d['user'],d['password'])
                time.sleep(2)

if __name__ == '__main__':
    report = REPORT_PATH + '\\test_pallet.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='自动化测试报告', description='用例执行情况:')
        runner.run(TestPurchase('test_login'))