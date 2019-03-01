# coding: utf-8
from fromework.base import BasePage
from selenium.webdriver.common.by import By
import time
from fromework.logger import Logger

logger=Logger(logger="PostContent").getlog()
class Four(BasePage):
    name = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    login_btn = (By.CSS_SELECTOR, '.pn em')

    def login(self, x, y):
        self.sendkeys(x, *self.name)
        self.sendkeys(y, *self.pwd)
        self.click(*self.login_btn)

    moren = (By.CSS_SELECTOR, '.bm_c h2 a')
    high_btn=(By.CSS_SELECTOR,'.bar a')
    vote=(By.CSS_SELECTOR,'.mbw li:last-child a')
    vote_title=(By.ID,'subject')
    text_one=(By.CSS_SELECTOR,'.mbm p input')
    text_two=(By.CSS_SELECTOR,'.mbm p:nth-last-child(5) input')
    text_three=(By.CSS_SELECTOR,'.mbm p:nth-last-child(4) input')
    text_content=(By.CSS_SELECTOR,'body')
    vote_btn=(By.ID,'postsubmit')

    def set_vote(self,t,one,two,three,con):
        time.sleep(2)
        self.click(*self.moren)
        self.click(*self.high_btn)
        self.click(*self.vote)
        self.sendkeys(t,*self.vote_title)
        self.sendkeys(one, *self.text_one)
        self.sendkeys(two, *self.text_two)
        self.sendkeys(three, *self.text_three)
        self.sendkeys(con, *self.text_content)
        self.click(*self.vote_btn)
        self.get_window_img()

    select_vote=(By.CSS_SELECTOR,'.pslt')
    select_submit=(By.ID,'pollsubmit')

    def submit_vote(self):
        self.click(*self.select_vote)
        self.click(*self.select_submit)
        self.get_window_img()

    vote_one_search=(By.CSS_SELECTOR, ".pvt label")
    vote_one_percent=(By.CSS_SELECTOR, ".pcht tr:nth-child(2) td:nth-child(2)")
    vote_two_search=(By.CSS_SELECTOR, ".pcht tr:nth-child(3) label")
    vote_two_percent=(By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:nth-child(2)")
    vote_three_search=(By.CSS_SELECTOR, ".pcht tr:nth-child(5) label")
    vote_three_percent=(By.CSS_SELECTOR, ".pcht tr:nth-child(6) td:nth-child(2)")

    vote_title_theme=(By.ID,'thread_subject')

    def con_and_theme(self):
        logger.info("第一个名称：%s" % self.find_element(*self.vote_one_search).text)
        logger.info("第一个比例：%s" % self.find_element(*self.vote_one_percent).text)
        logger.info("第二个名称：%s" % self.find_element(*self.vote_two_search).text)
        logger.info("第二个比例：%s" % self.find_element(*self.vote_two_percent).text)
        logger.info("第三个名称：%s" % self.find_element(*self.vote_three_search).text)
        logger.info("第三个比例：%s" % self.find_element(*self.vote_three_percent).text)


