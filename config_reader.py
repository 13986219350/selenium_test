import configparser
import os


class ConfigReader:
    def __init__(self, config_file="E:\PycharmProjects\selenium_test\config\config.ini"):
        self.config_reader = configparser.ConfigParser()
        self.config_file = config_file
        self.config = {}
        self.parser_config()

    def parser_config(self):
        try:
            self.config_reader.read(self.config_file)
            # 遍历配置信息
            for section in self.config_reader.sections():  # 获取所有节
                print(f"Section: {section}")
                for option in self.config_reader.options(section):  # 获取每个节中的选项
                    value = self.config_reader.get(section, option)  # 获取选项的值
                    if section not in self.config:
                        self.config[section] = {}
                    self.config[section][option] = value
            print("全部配置：", self.config)
        except Exception as e:
            raise Exception(f"Error reading config file '{self.config_file}': {e}")
