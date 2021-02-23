#!usr/bin/env python
# -*- coding:utf-8 -*-

from web.selenium_windows.Base import Base

from time import sleep
class TestWindows(Base):


    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.switch_to_window(windows[0])
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('18930336292')
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('chen1998')
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)
#TODO:一种是无头模式，另一种是类似黑名单   图片验证或者让图片变为正方向验证