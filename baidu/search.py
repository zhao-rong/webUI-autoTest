from fromework.base import BasePage
from selenium.webdriver.common.by import By


class BaiduSearch(BasePage):
    search_text=(By.ID ,'kw')
    search_btn=(By.CSS_SELECTOR,'.s_btn_wr .s_btn')

    def search(self,text):
        self.sendkeys(text,*self.search_text)
        self.click(*self.search_btn)
