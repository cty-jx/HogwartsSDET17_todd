#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.test_selenium.login_page.add_page import AddPage
from web.test_selenium.login_page.login_page import LoginPage
from web.test_selenium.login_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()
        # 将类初始化成对象
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)

    def goto_add(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        return AddPage(self.driver)