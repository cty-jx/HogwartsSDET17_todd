#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 被测类：计算器
import logger

class Calculator:
    def add(self, a, b):
        logger.info(f"This case is to test {a} + {b}")
        return a + b

    def subtract(self, a, b):
        logger.info(f"This case is to test {a} - {b}")
        return a - b

    def multiply(self, a, b):
        logger.info(f"This case is to test {a} * {b}")
        return a * b

    def div(self, a, b):
        logger.info(f"This case is to test {a} / {b}")
        return a / b
