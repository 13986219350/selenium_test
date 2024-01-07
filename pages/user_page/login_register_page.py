from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element_dict = {
    '注册-邮箱': (By.XPATH, '//*[@class="card"][2]//*[@placeholder="邮箱地址"]'),
    '注册-密码': (By.XPATH, '//*[@class="card"][2]//*[@placeholder="密码"]'),
    '注册-确认密码': (By.XPATH, '//*[@class="card"][2]//*[@placeholder="确认密码"]'),
    '注册': (By.XPATH, '(//*[@class="btn btn-dark btn-lg w-100 fw-bold"])[2]'),
}


class LoginRegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def register_input_email(self, email):
        # self.driver.find_element(*element_dict["注册-邮箱"]).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(element_dict["注册-邮箱"])).send_keys(email)

    def register_input_password(self, password):
        # self.driver.find_element(*element_dict["注册-密码"]).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(element_dict["注册-密码"])).send_keys(password)

    def register_input_password_confirm(self, password):
        # self.driver.find_element(*element_dict["注册-确认密码"]).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(element_dict["注册-确认密码"])).send_keys(password)

    def click_register_button(self):
        # self.driver.find_element(*element_dict["注册"]).click()
        self.wait.until(EC.visibility_of_element_located(element_dict["注册"])).click()

    def register(self, email, password):
        self.register_input_email(email)
        self.register_input_password(password)
        self.register_input_password_confirm(password)
        self.click_register_button()


if __name__ == '__main__':
    pass
