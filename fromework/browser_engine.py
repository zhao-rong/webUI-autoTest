import os
from selenium import webdriver
from fromework.logger import Logger
from configparser import ConfigParser

logger=Logger('BrowserEngine').getlog()

class BrowserEngine():
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_path=dir+'/tools/chromedriver.exe'
    firefox_path = dir + '/tools/geckodriver.exe'
    ie_path = dir + '/tools/IEDriverServer.exe'
    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get('browsersType','browserName')
        logger.info('You had select %s browser'% browser)
        url=config.get('testServer','URL')
        logger.info('The test server url is %s'%url)

        if browser=='Firefox':
            driver=webdriver.Firefox(executable_path=self.firefox_path)
            logger.info('Open Firefox browser')
        elif browser =='Chrome':
            driver=webdriver.Chrome(self.chrome_path)
            logger.info('Open Chrome browser')
        else:
            driver=webdriver.Ie(self.ie_path)
            logger.info('Open Ie browser')
        driver.get(url)
        logger.info('Open url %s'%url)
        driver.maximize_window()
        logger.info('Maximize the current window')
        driver.implicitly_wait(10)
        logger.info('Set implicitly wait 10 seconds')
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info('Close and quit the browser')