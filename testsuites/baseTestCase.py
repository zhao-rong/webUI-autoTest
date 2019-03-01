import unittest
from selenium import webdriver
from fromework.browser_engine import BrowserEngine


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser=BrowserEngine()
        self.driver=browser.open_browser()

        # self.driver = webdriver.Chrome('../tools/chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)


    def tearDown(self):
        self.driver.quit()
