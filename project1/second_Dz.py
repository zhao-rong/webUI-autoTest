# coding: utf-8
from fromework.base import BasePage
from selenium.webdriver.common.by import By
import time

class Second(BasePage):
    name = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    login_btn = (By.CSS_SELECTOR, '.pn em')

    def Alogin(self,x,y):
        self.sendkeys(x,*self.name)
        self.sendkeys(y,*self.pwd)
        self.click(*self.login_btn)

    moren = (By.LINK_TEXT, '默认版块')
    tie_box = (By.CSS_SELECTOR,'.o input')
    delete=(By.CSS_SELECTOR,'#mdly p a')
    queren = (By.ID, 'modsubmit')

    def delete_tie(self):
        time.sleep(2)
        self.click(*self.moren)
        self.click(*self.tie_box)
        self.click(*self.delete)
        self.get_window_img()
        self.click(*self.queren)

    manage=(By.LINK_TEXT,'管理中心')
    # mima=(By.NAME,'admin_password')
    # tijiao=(By.CSS_SELECTOR,'btn')
    luntan=(By.ID,'header_forum')
    addnew=(By.CSS_SELECTOR,'.lastboard a')
    # new_name=(By.CSS_SELECTOR,'form .tb2 tbody:nth-last-child(2) .board .txt')
    tijiao_a=(By.NAME,'editsubmit')

    def new_bankuai(self):
        self.click(*self.manage)
        self.switch_handle()
        # self.sendkeys(m,*self.mima)
        # self.click(*self.tijiao)
        self.click(*self.luntan)
        self.get_window_img()
        self.iframe()
        self.click(*self.addnew)
        # self.sendkeys(b,*self.addnew)
        self.click(*self.tijiao_a)

    tuichu = (By.LINK_TEXT, '退出')

    def loginout(self):
        self.switch_handle()
        self.click(*self.tuichu)
        self.click(*self.tuichu)

    p_name = (By.NAME, 'username')
    p_pwd = (By.NAME, 'password')
    p_login_btn = (By.CSS_SELECTOR, '.pn em')

    def Plogin(self,x,y):
        self.sendkeys(x, *self.p_name)
        self.sendkeys(y, *self.p_pwd)
        self.click(*self.p_login_btn)

    new_bankuai_tie = (By.CSS_SELECTOR, 'tbody .fl_row:nth-last-child(2) h2 a')
    title = (By.ID,'subject')
    content = (By.NAME,'message')
    fatie_btn = (By.CSS_SELECTOR, '.pnpost button')

    def fatie(self, t, c):
        time.sleep(2)
        self.click(*self.new_bankuai_tie)
        self.sendkeys(t, *self.title)
        self.sendkeys(c, *self.content)
        self.click(*self.fatie_btn)
        self.get_window_img()

    reply_con = (By.ID, 'fastpostmessage')
    reply_btn = (By.ID, 'fastpostsubmit')

    def reply(self, r):
        self.switch_handle()
        time.sleep(20)
        self.sendkeys(r, *self.reply_con)
        self.click(*self.reply_btn)