#!usr/bin/env python
# -*- coding:utf-8 -*-
from web.selenium_windows.Base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_window("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)