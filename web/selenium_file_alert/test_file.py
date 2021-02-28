#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from web.selenium_windows.Base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("http://image.baidu.com/")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys(r'F:\其他\2194005462\preview.jpg')
        time.sleep(4)