# coding: utf-8
from fromework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Third(BasePage):
    name = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    login_btn = (By.CSS_SELECTOR, '.pn em')

    def login(self, x, y):
        self.sendkeys(x, *self.name)
        self.sendkeys(y, *self.pwd)
        self.click(*self.login_btn)

    sch_text=(By.NAME,'srchtxt')
    sch_btn=(By.CSS_SELECTOR,'.pnc')
    tie_name_link=(By.CSS_SELECTOR,'.xs3 font')
    tie_name=(By.ID,'thread_subject')

    def search(self,a):
        time.sleep(2)
        self.click(*self.sch_text)
        self.sendkeys(a,*self.sch_text)
        self.click(*self.sch_btn)
        time.sleep(2)
        self.get_window_img()
        self.switch_handle()
        self.click(*self.tie_name_link)
        time.sleep(2)
        self.switch_handle()
        self.get_window_img()
        title = self.find_element(*self.tie_name).text
        return title

    tuichu = (By.LINK_TEXT, '退出')

    def loginout(self):
        self.click(*self.tuichu)