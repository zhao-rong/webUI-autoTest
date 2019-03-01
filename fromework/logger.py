import logging
import os,time

class Logger():
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rt=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+"/logs/"
        log_name=log_path+rt+'.log'
        fh= logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger
