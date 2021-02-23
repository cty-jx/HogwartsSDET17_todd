#!usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("365787853")
        self.driver.find_element_by_id("user_password").send_keys("ctyjx1998")
        sleep(3)
        element = self.driver.find_element_by_css_selector('#user_remember_me')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_elements_by_xpath('//*[@id="new_user"]/div[4]/input')
