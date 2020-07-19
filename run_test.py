import unittest
from common.logger import log
from common.HTMLTestRunner import HTMLTestRunner
from common.constant import constant
import os
import time
import pytest

# if __name__ == '__main__':
#     log.info('---------------------------------------测试开始---------------------------------------')
#     # 创建测试套件
#     suite = unittest.TestSuite()
#
#     # 加载测试用例套件
#     loader = unittest.TestLoader()
#     # 此处匹配文件名以“test”开头的“.py”类型的文件
#     suite.addTest(loader.discover(constant.CASES_DIR))
#     # HTMLTestRunner 生成测试报告
#     # 时间戳
#     # name = time.strftime("[%Y-%m-%d] [%H-%M-%S]", time.localtime())+'.html'
#     with open(file=os.path.join(constant.REPORTS_DIR, 'report.html'), mode='wb') as fb:
#         runner = HTMLTestRunner(stream=fb, title='测试报告', description='日常发布测试', tester='石高林')
#         runner.run(suite)
#     log.info('---------------------------------------测试结束---------------------------------------')
if __name__ == '__main__':
    # pytest.main(['-s', '-m "success"', '--html={}'.format(os.path.join(constant.REPORTS_DIR, 'report.html'))])
    # 使用 allure
    pytest.main(['-s', '-m "success"', f'--alluredir={constant.Allure_DIR}'])
