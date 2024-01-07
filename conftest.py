import os
import pytest
import allure

from utils.driver_manager import DriverManager
from utils.config_reader import ConfigReader
from pages.user_page.base_page import BasePage

driver = None
# Fixture: 初始化 WebDriver
@pytest.fixture(scope="function")
def get_driver():
    global driver
    driver = DriverManager.get_driver()
    driver.get("http://localhost")
    driver.maximize_window()
    driver.implicitly_wait(10)
    base_page = BasePage(driver)
    base_page.switch_to_cn()
    yield driver
    DriverManager.quit_driver()


# Fixture: 读取测试数据
@pytest.fixture(scope="function")
def test_data():
    # 可以根据需要从测试数据文件中读取数据
    data = {"username": "user1", "password": "pass1"}
    return data


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


if __name__ == '__main__':
    pass
