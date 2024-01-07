from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, 0.3)

    def switch_to_cn(self):
        language = self.driver.find_element(By.ID, 'language-dropdown')
        ActionChains(self.driver).move_to_element(language).perform()
        # self.driver.find_element(By.LINK_TEXT, "中文").click()
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "中文"))).click()


if __name__ == '__main__':
    pass
