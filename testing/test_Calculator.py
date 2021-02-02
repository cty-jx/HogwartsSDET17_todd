#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
import yaml
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    # return (datas['add']['datas'], datas['add']['ids'])

    return datas


@pytest.fixture(params=get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
def get_datas_with_fixture(request):
    return request.param


def test_param(get_datas_with_fixture):
    print(get_datas_with_fixture)


# yaml json excel csv xml
# 测试类


@pytest.fixture()
def get_instance():
    print("开始计算")
    calc: Calculator = Calculator()
    yield calc
    print("结束计算")


@allure.feature("计算器")
class TestCalc:
    datas: list = get_datas()
    calc: Calculator = Calculator()

    @allure.title("相加_{get_datas_with_fixture[0]}_{get_datas_with_fixture[1]}")
    @allure.story("相加功能")
    def test_add1(self, get_instance, get_datas_with_fixture):
        f = get_datas_with_fixture
        assert f[2] == get_instance.add(f[0], f[1])

    @allure.title("相加")
    @allure.story("相加功能")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    @allure.story("相减功能")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()['subtract']['datas'], ids=get_datas()['subtract']['ids'])
    def test_subtract(self, a, b, expect):
        result = self.calc.subtract(a, b)
        assert expect == result

    @allure.story("相乘功能")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()['multiply']['datas'], ids=get_datas()['multiply']['ids'])
    def test_multiply(self, a, b, expect):
        result = self.calc.multiply(a, b)
        assert expect == result

    @allure.title("相除")
    @allure.story("相除功能")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
    def test_div(self, a, b, expect):
        if b == 0:
            try:
                self.calc.div(a, b)
            except ZeroDivisionError as e:
                print("除数不能为0")
        else:
            result = self.calc.div(a, b)
            assert result == expect


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
