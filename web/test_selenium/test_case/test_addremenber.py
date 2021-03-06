#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

from web.test_selenium.login_page.main_page import MainPage


class TestAddMember:
    def test_add(self):
        main = MainPage()
        a = main.goto_add()
        a.save_member()

