from selenium.webdriver.common.by import By

# url
url = r'http://192.168.250.202:9999/'

# 用户名
# username = By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[1]/div/div[1]/input'

# 密码
# password = By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/input'

# 用户名
username = By.CLASS_NAME, 'el-input__inner'
name_num = 0

# 密码
password = By.CLASS_NAME, 'el-input__inner'
pwd_num = 1

# 登录按钮
login = By.CLASS_NAME, 'el-button'

# # 异常信息
# error = By.CLASS_NAME, 'login-box-title'

# # 通过信息
# succeed = By.CLASS_NAME, 'login-box2'

# 创建考试按钮
create = By.CLASS_NAME, 'el-button'
created_num = 0

# 考试名称
ksmc = By.CLASS_NAME, 'el-input__inner'
mc_num = 0

# 考试区域
ksqy = By.CLASS_NAME, 'el-input__inner'
qy_num = 1
# 考试区域下拉框选中
ksqy_xz = By.CLASS_NAME, 'el-cascader__suggestion-item'

# 考试时间
kssj = By.CLASS_NAME, 'el-range-input'
# 开始时间
time_bgn = 0
# 结束时间
time_end = 1

# 考试标签
ksbq = By.CSS_SELECTOR, '.el-radio-group .el-radio__inner'

# 考试年级
ksnj_one = By.CLASS_NAME, 'el-input__inner'
ksnj_num = 3
ksnj_two = By.CLASS_NAME, 'el-select-dropdown__item'

# 考试科目
kskm = By.CLASS_NAME, 'el-checkbox__inner'

# 按钮
an = By.CLASS_NAME, 'el-button'
# 取消
an_quit = 0
# 确定
an_ok = 1
# 确定后需要再次确定
an_ook = 3

# 获取断言
hqdy = By.CLASS_NAME, 'home-exam-name'
hqdy_num = 0

