from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_reader import ConfigReader
from utils import config



class DriverManager:
    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            browser = config["webdriver"]["browser"]  # 这里可以根据需要设置浏览器类型，也可以从配置文件读取
            cls.driver = cls.create_driver(browser)
        return cls.driver

    @classmethod
    def create_driver(cls, browser):
        if browser.lower() == "chrome":
            return cls.create_chrome_driver()
        elif browser.lower() == "firefox":
            return cls.create_firefox_driver()
        # 如果需要添加其他浏览器的支持，可以在这里继续添加相应的实现

    @classmethod
    def create_chrome_driver(cls):
        options = Options()
        is_headless = config["webdriver"]["headless"].lower() == "true"
        if is_headless:
            options.add_argument("--headless")  # 例如：设置 Chrome 为无头模式
            options.add_argument("window-size=1920x1080")
        return webdriver.Chrome(options=options)

    @classmethod
    def create_firefox_driver(cls):
        # 在这里添加创建 Firefox WebDriver 的逻辑
        pass

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None

if __name__ == '__main__':
    print(bool("false"))