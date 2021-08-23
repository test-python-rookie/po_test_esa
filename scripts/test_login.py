import unittest
from parameterized import parameterized
from page.page_login import PageLogin
from time import sleep
from base.get_driver import GetDriver

def get_data():
    return [('admin', '1234', 'http://192.168.250.202:9999/esa.html#/exam'),
            ('admin01', '1234', 'http://192.168.250.202:9999/esa.html#/exam')]

class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 获取登录页面对象
        self.login = PageLogin(GetDriver().get_driver())

    # 结束方法
    def tearDown(self):
        # 关闭浏览器
        GetDriver().quit_driver()

    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, password, expect):
        # 调用测试登录方法
        self.login.page_login(username, password)
        sleep(2)
        # 调用测试登录后的信息
        msg = self.login.page_login_assert()
        try:

            self.assertEqual(msg, expect)
            print('登录成功！！！')
            print('url地址为：', msg)
        except AssertionError:
            self.login.page_login_errorview()
            print('登录失败！！！')
            print('url地址为：', msg)