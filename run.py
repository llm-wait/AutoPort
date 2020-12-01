import unittest

import time

from Postman.tool.datastore import TestOne
from Postman.tool.htmlTestRunner import HTMLTestRunner
from Postman.tool.project_path import test_report_parh
from Postman.tool.test_http import TestHttp

suit=unittest.TestSuite()
load=unittest.TestLoader()
suit.addTest(load.loadTestsFromTestCase(TestOne))

#执行
report_now=time.strftime('%Y-%m-%d_%H_%M_%S')
with open(test_report_parh+"/result_"+report_now+".html",'wb')as f:
    runner=HTMLTestRunner(stream=f, title='系统接口',description='系统接口测试')
    runner.run(suit)
#jekins密码51bee3607a5b4b25b211256ebe402e66