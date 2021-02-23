#!usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver  # 浏览器驱动器
from selenium.webdriver.common.by import By  # 定位器


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # sleep(5)
        # self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys("三国志幻想大陆")
        self.driver.find_element(By.ID,'su').click()
        print("hello")