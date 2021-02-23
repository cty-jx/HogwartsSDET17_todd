#!usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver  # 浏览器驱动器
from selenium.webdriver.common.by import By  # 定位器
from selenium.webdriver.common.keys import Keys  # 键盘对象
from selenium.webdriver.support import expected_conditions as EC  # 判断器
from selenium.webdriver.support.wait import WebDriverWait  # 浏览器等待对像
import time


class TestTodd:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        time.sleep(1)
        self.driver.find_element(By.ID, "su").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 - 主页").click()
