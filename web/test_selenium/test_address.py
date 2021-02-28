#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
class TestTemp:
    def test_address(self):

        chrome_arg = webdriver.ChromeOptions()

        chrome_arg.debugger_address = '192.168.0.109:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.find_element(By.XPATH,"")