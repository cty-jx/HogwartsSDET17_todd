#!usr/bin/env python
# -*- coding:utf-8 -*-

import pytest

from pytest_encode import logger


@pytest.mark.parametrize('name', ['陈天雨','罗杰'])
def test_encode(name):
    logger.info(f'测试数据{name}')
    print(name)
