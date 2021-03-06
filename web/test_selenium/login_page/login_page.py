#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from web.test_selenium.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)