from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Check(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, 0.3)

    def check_element_exists(self, element, exist):
        try:
            self.wait.until(EC.visibility_of_element_located(element))
            find = True
        except TimeoutException:
            find = False
        assert find == exist
