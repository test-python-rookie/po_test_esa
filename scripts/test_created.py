import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
from page.page_created import PageCreated
from time import sleep
from selenium.webdriver.common.keys import Keys

def get_data():
    return [('【0823】联考测试', '赤坎区', '2021-08-20', ('2021-08-25', Keys.ENTER), 4, 3, 2, '【0823】联考测试')]

class TestCreated(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.created = PageCreated(GetDriver().get_driver())

    # 结束方法
    def tearDown(self):
        # 关闭浏览器
        GetDriver().quit_driver()
        pass
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_created(self, ksmc, ksqy, kssj, jssj, ksbq, ksnj, kskm, expect):
        # 调用测试方法
        self.created.page_created(ksmc, ksqy, kssj, jssj, ksbq, ksnj, kskm)
        sleep(3)
        # 获取断言
        msg = self.created.page_created_pass()
        try:
            self.assertEqual(msg, expect)
            print('创建考试成功！！！')
            print('考试名称为：', msg)
        except AssertionError:
            self.created.page_created_errorview()
            print('创建考试失败！！！')
            print('考试名称为：', msg)
