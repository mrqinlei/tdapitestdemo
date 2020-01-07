#coding=utf-8
from BeautifulReport import BeautifulReport
import unittest
import os
import time
from demo import TestRun
from Sendmail import SendEmail

class BaseFlow:
    def __init__(self):
        self.send_mail = SendEmail()


    def run_case(self):
        now = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))

        # 报告地址&名称
        report_title = 'AutoTestReport' + now + ".html"     # 如果不能打开这个文件，可能是now的格式，不支持：和空格

        report_path = os.getcwd() + '/report/'
        print(report_path)
        if not os.path.exists(report_path):
            os.makedirs(report_path)
        #filename = ''.join([report_path + now + '-result.html'])

        # 报告描述
        desc = '用于展示修改样式后的HTMLTestRunner'
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestRun))
        # unittest.TextTestRunner().run((suite))
        runner = BeautifulReport(suite)
        runner.report(description=desc, filename=report_title, report_dir=report_path)
        #self.send_mail.send_mail()




if __name__=='__main__':
    run = BaseFlow()
    run.run_case()