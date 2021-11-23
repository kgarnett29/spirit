import os
import re
import sys
import sys
import os
import urllib.request
import time
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
os.environ['DJANGO_SETTINGS_MODULE']='apps.settings'  #配置系统变量
import django
django.setup()
from common import config
logfilename=config.DJANGO_RUN_CHK_LOG
######################################################################################
import logging
from logging.handlers import RotatingFileHandler
LOG_MODE = 'a'
LOG_MAX_SIZE = 10*1024*1024 # 2M
LOG_MAX_FILES = 1
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s [%(levelname)-10s]  %(message)s"
handler = RotatingFileHandler(logfilename, LOG_MODE, LOG_MAX_SIZE, LOG_MAX_FILES)
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
Logger = logging.getLogger()
Logger.setLevel(LOG_LEVEL)
Logger.addHandler(handler)
#######################################################################################

def getProcessInfo(processName):
    command = "ps -ef|grep "+processName
    r = os.popen(command)
    logging.info(command)
    cmd_result = r.read()
    logging.info(cmd_result)
    r.close()
    if cmd_result=="":
        logging.error("exec cmd failed!")
    else:
        run_mod='runserver'
        m=re.search(run_mod,cmd_result)
        if m is not None:
            logging.info(m.group(0))
            logging.info("django process is running!")
        else:
            p=os.popen(config.AIO_PATH_STARTUP)
            q = os.popen(config.AIO_DJANGO_CRONTAB)
            logging.error("django process is not running!")
            logging.info(p)
            logging.info(q)

def main():
    getProcessInfo("manage.py")

if __name__ == '__main__':
    main()
