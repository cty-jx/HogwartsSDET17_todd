#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pytest
from web.selenium_windows.Base import Base
from selenium.common.exceptions import NoSuchElementException

class TestJS(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenim测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        try:
            xpath = "//*[@id='page']/div/a[9]/span[2]"
            self.driver.find_element_by_xpath(xpath).click()
        except NoSuchElementException:
            print("没有找到该元素")
        for code in ['return document.title','return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("a = document.getElementById('train_date').value='2021-02-27'")
        time.sleep(3)