#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddPage:
    def __init__(self, driver):
        self.driver = driver

    def save_member(self):
        def wait_name(driver):
            driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tood_cty")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("tood_cty")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("15008261473")
        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()