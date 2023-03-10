import time
import os
from selenium import webdriver
from src.utils.config import DRIVER_PATH, REPORT_PATH, UPLOAD_PICTURE_PATH
from selenium.common.exceptions import NoSuchElementException

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30, open = False):
        if open == True:
            self.driver = webdriver.Chrome()
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def delete_screen_shot(self):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        
        lists = os.listdir(screenshot_path)
        lists.sort(key=lambda fn:os.path.getmtime(screenshot_path +'\\'+fn))
        file_new = os.path.join(screenshot_path,lists[-1])
        os.remove(file_new)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def isElementExistence(self, *args):
        try:
            self.driver.find_element(*args)
            return True
        except:
            return False

    # 该方法会实现自动上传一张默认图片，但是存放exe文件的路径必须是：当前运行脚本的同目录..\external\upload_picture.exe
    # 因为上传图片无法通过selenium+python直接做到，需要用到录制的exe文件
    def upload_picture(self,Xpath = UPLOAD_PICTURE_PATH):
        os.system(Xpath)

    def handle_switch(self,page = -1):
        handle = self.driver.window_handles #获取当前句柄b
        self.driver.switch_to.window(handle[page]) #在句柄2执行