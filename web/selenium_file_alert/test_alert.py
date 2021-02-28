#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver import ActionChains
from web.selenium_windows.Base import Base


class TestAlert(Base):
    def test_alert(self):

        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        time.sleep(2)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        print("点击alert确认")
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        time.sleep(3)
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)