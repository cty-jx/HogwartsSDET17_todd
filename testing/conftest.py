#!/usr/bin/env python
# -*- coding: utf-8 -*-
# conftest.py 文件名字是固定的，不能改
from typing import List

import pytest
import yaml
from logger import logger


def get_datas(name, type='int'):
    with open("./datas/calc.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return datas, ids


@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_add_int_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('add', 'float')[0], ids=get_datas('add', 'float')[1])
def get_add_float_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('subtract', 'int')[0], ids=get_datas('subtract', 'int')[1])
def get_subtract_int_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('subtract', 'float')[0], ids=get_datas('subtract', 'float')[1])
def get_subtract_float_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('multiply', 'int')[0], ids=get_datas('multiply', 'int')[1])
def get_multiply_int_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('multiply', 'float')[0], ids=get_datas('multiply', 'float')[1])
def get_multiply_float_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('div', 'int_normal')[0], ids=get_datas('div', 'int_normal')[1])
def get_div_int_normal_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param


@pytest.fixture(params=get_datas('div', 'int_error')[0], ids=get_datas('div', 'int_error')[1])
def get_div_int_error_datas_with_fixture(request):
    logger.info(f'数据类型为{request.param}')
    return request.param

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    items.reverse()