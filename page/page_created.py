import page
from base.base import Base
from page.page_login import PageLogin
from time import sleep

class PageCreated(Base):
    # 登录
    # def __init__(self, driver):
    #     self.page_login = PageLogin(driver)
    #     self.page_login.page_login('admin01', '1234')
    #     self.driver = Base(self.page_login)
    # 输入用户名、密码
    def page_login_user(self):
        # 用户名
        self.base_input(page.username, "admin01", page.name_num)
        # 密码
        self.base_input(page.password, "1234", page.pwd_num)

    # 点击登录
    def page_login_btn(self):
        self.base_click(page.login)

    # 点击创建
    def page_created_create(self):
        self.base_click(page.create, page.created_num)

    # 输入考试名称
    def page_created_ks(self, ksmc, ksqy, kssj, jssj, ksbq, ksnj, kskm):
        # 考试名称
        self.base_input(page.ksmc, ksmc, page.mc_num)
        # 考试区域
        self.base_input(page.ksqy, ksqy, page.qy_num)
        self.base_click(page.ksqy_xz)
        # 考试时间
        self.base_input(page.kssj, kssj, page.time_bgn)
        self.base_input(page.kssj, jssj, page.time_end)
        # 考试标签
        self.base_click(page.ksbq, ksbq)
        # 考试年级
        self.base_click(page.ksnj_one, page.ksnj_num)
        sleep(1)
        self.base_click(page.ksnj_two, ksnj)
        sleep(1)
        # 考试科目
        self.base_click(page.kskm, kskm)
        # 取消创建考试
        self.base_click(page.an, page.an_quit)
        # 确定创建考试
        # self.base_click(page.an, page.an_ok)
        # self.base_click(page.an, page.an_ook)

    # 获取断言
    def page_created_pass(self):
        return self.base_get_text(page.hqdy, page.hqdy_num)

    # 截图
    def page_created_errorview(self):
        self.base_get_image()

    # 组装业务方法
    def page_created(self, ksmc, ksqy, kssj, jssj, ksbq, ksnj, kskm):
        self.page_login_user()
        self.page_login_btn()
        sleep(2)
        self.page_created_create()
        self.page_created_ks(ksmc, ksqy, kssj, jssj, ksbq, ksnj, kskm)
