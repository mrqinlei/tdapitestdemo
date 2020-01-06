from BeautifulReport import BeautifulReport
import unittest
import os
from apitest import RunMain
import time
from demo import TestRun



now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 报告地址&名称
report_title = '用例报告' + now + ".html"     # 如果不能打开这个文件，可能是now的格式，不支持：和空格

report_path = os.getcwd() + '/report/'
if not os.path.exists(report_path):
    os.makedirs(report_path)
#filename = ''.join([report_path + now + '-result.html'])

# 报告描述
desc = '用于展示修改样式后的HTMLTestRunner'

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRun))
    #unittest.TextTestRunner().run((suite))
    runner = BeautifulReport(suite)
    runner.report(description=desc,filename=report_title,log_path=report_path)
