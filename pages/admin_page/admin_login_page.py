from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element_dict = {
    "邮箱": (By.ID, "email-input"),
    "密码": (By.ID, "password-input"),
    "登录": (By.XPATH, '//button[@type="submit"]')
}


class AdminLoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://localhost/admin")
        self.wait = WebDriverWait(self.driver, 5, 0.3)

    def login(self, email, password):
        # self.driver.find_element(*element_dict["邮箱"]).send_keys(email)
        # self.driver.find_element(*element_dict["密码"]).send_keys(password)
        # self.driver.find_element(*element_dict["登录"]).click()
        self.wait.until(EC.visibility_of_element_located(element_dict["邮箱"])).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(element_dict["密码"])).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(element_dict["登录"])).click()


if __name__ == '__main__':
    pass
