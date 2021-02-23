#!usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep

import pytest
from selenium import webdriver  # 浏览器驱动器
from selenium.webdriver import TouchActions
from selenium.webdriver.common.keys import Keys

class TestTouchAction():

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchAction(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele,0,2000).perform()
        sleep(3)