# coding: utf-8
import unittest,os
from testsuites.test_first_login import Test_login
from testsuites.test_second_Dz import Test_second
from testsuites.test_thrid import Test_Third
from testsuites.test_four_Dz import Test_Four
import HTMLTestRunner

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,'result')
if not os.path.exists(report_path):
    os.mkdir(report_path)

suites=unittest.TestSuite()
suites.addTest(unittest.makeSuite(Test_login))
suites.addTest(unittest.makeSuite(Test_second))
suites.addTest(unittest.makeSuite(Test_Third))
suites.addTest(unittest.makeSuite(Test_Four))

if __name__=='__main__':
    html_report=report_path + r"\report.html"
    fp=open(html_report,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,
             title="单元测试报告",description="用例执行情况")
    runner.run(suites)