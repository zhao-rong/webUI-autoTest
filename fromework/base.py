import os,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fromework.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains

logger=Logger(logger="BasePage").getlog()

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    #返回
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    #前进
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
     #打开网页
    def open_url(self,url):
        self.driver.get(url)
        logger.info("Open page.")
     #退出浏览器
    def quit_browser(self):
        self.driver.quit()
        logger.info("Quit browser.")
    #关闭某个浏览器页面
    def close(self):
        self.driver.close()
        logger.info("Close  page.")
    #查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("找到页面元素")
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.error("页面中未能找到元素",e)

    #清除
    def clear(self,*loc):
        e1=self.find_element(*loc)
        try:
            e1.clear()
            logger.info('Clear text in input box before typing')
        except Exception as e:
            logger.error('Failed to clear text in input box with%s'% e)

    # 传值
    def sendkeys(self, text, *loc):
        e1 = self.find_element(*loc)
        # e1.clear()
        try:
            e1.send_keys(text)
            logger.info("输入内容")
        except Exception as e:
            logger.error('Failed to type in input box with%s' % e)
    #点击
    def click(self,*loc):
        e1 = self.find_element(*loc)
        try:
            e1.click()
            logger.info('Click and open another page')
        except Exception as e:
            logger.error('Failed to click  with%s' % e)

    #截图
    def get_window_img(self):
        file_path = os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder : /screenshots')
        except Exception as e:
            self.get_window_img()
            logger.error('Failed to take screenshot %s' % e)

    #切换窗口
    def switch_handle(self):
        window_list=self.driver.window_handles
        self.driver.switch_to.window(window_list[len(window_list)-1])
        logger.info('Swich to window handle')

    def iframe(self):
        self.driver.switch_to.frame(0)
