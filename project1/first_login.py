# coding: utf-8
from fromework.base import BasePage
from selenium.webdriver.common.by import By
import time

class First(BasePage):
    name = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    login_btn = (By.CSS_SELECTOR, '.pn em')

    def login(self,x,y):
        self.sendkeys(x,*self.name)
        self.sendkeys(y,*self.pwd)
        self.click(*self.login_btn)

    moren = (By.CSS_SELECTOR, '.bm_c h2 a')
    title = (By.CSS_SELECTOR, '.pbt .px')
    content = (By.CSS_SELECTOR, '.area .pt')
    fatie_btn = (By.CSS_SELECTOR, '.pnpost')

    def fatie(self, t, c):
        time.sleep(2)
        self.click(*self.moren)
        self.sendkeys(t, *self.title)
        self.sendkeys(c, *self.content)
        self.click(*self.fatie_btn)
        self.get_window_img()

    reply_con = (By.ID, 'fastpostmessage')
    reply_btn = (By.ID, 'fastpostsubmit')

    def reply(self,r):
        self.sendkeys(r,*self.reply_con)
        self.click(*self.reply_btn)
        self.get_window_img()

    tuichu = (By.LINK_TEXT, '退出')

    def loginout(self):
        self.click(*self.tuichu)
