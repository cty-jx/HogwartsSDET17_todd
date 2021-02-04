#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import allure
import pytest
sys.path.append('..')
from pythoncode.Calculator import Calculator

#
# def get_datas():
#     with open("./datas/calc.yml") as f:
#         datas = yaml.safe_load(f)
#     return datas


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

    @allure.title("add_{get_add_int_datas_with_fixture[0]}_{get_add_int_datas_with_fixture[1]}")
    @allure.story("Add Integer Function")
    def test_add_int(self, get_instance, get_add_int_datas_with_fixture):
        add_int = get_add_int_datas_with_fixture
        assert add_int[2] == get_instance.add(add_int[0], add_int[1])

    @allure.title("add_{get_add_float_datas_with_fixture[0]}_{get_add_float_datas_with_fixture[1]}")
    @allure.story("Add float Function")
    def test_add_float(self, get_instance, get_add_float_datas_with_fixture):
        add_float = get_add_float_datas_with_fixture
        assert add_float[2] == round(get_instance.add(add_float[0], add_float[1]), 8)

    @allure.title("subtract_{get_subtract_int_datas_with_fixture[0]}_{get_subtract_int_datas_with_fixture[1]}")
    @allure.story("subtract Integer Function")
    def test_subtract_int(self, get_instance, get_subtract_int_datas_with_fixture):
        subtract_int = get_subtract_int_datas_with_fixture
        assert subtract_int[2] == get_instance.subtract(subtract_int[0], subtract_int[1])

    @allure.title("subtract_{get_subtract_float_datas_with_fixture[0]}_{get_subtract_float_datas_with_fixture[1]}")
    @allure.story("subtract float Function")
    def test_subtract_float(self, get_instance, get_subtract_float_datas_with_fixture):
        subtract_float = get_subtract_float_datas_with_fixture
        assert subtract_float[2] == round(get_instance.subtract(subtract_float[0], subtract_float[1]), 8)

    @allure.title("multiply_{get_multiply_int_datas_with_fixture[0]}_{get_multiply_int_datas_with_fixture[1]}")
    @allure.story("multiply Integer Function")
    def test_multiply_int(self, get_instance, get_multiply_int_datas_with_fixture):
        multiply_int = get_multiply_int_datas_with_fixture
        assert multiply_int[2] == get_instance.multiply(multiply_int[0], multiply_int[1])

    @allure.title("multiply_{get_multiply_float_datas_with_fixture[0]}_{get_multiply_float_datas_with_fixture[1]}")
    @allure.story("multiply float Function")
    def test_multiply_float(self, get_instance, get_multiply_float_datas_with_fixture):
        multiply_float = get_multiply_float_datas_with_fixture
        assert multiply_float[2] == round(get_instance.multiply(multiply_float[0], multiply_float[1]), 8)

    @allure.title("div_{get_div_int_normal_datas_with_fixture[0]}_{get_div_int_normal_datas_with_fixture[1]}")
    @allure.story("div Integer normal Function")
    def test_div_int_normal(self, get_instance, get_div_int_normal_datas_with_fixture):
        div_int_normal = get_div_int_normal_datas_with_fixture
        assert div_int_normal[2] == get_instance.div(div_int_normal[0], div_int_normal[1])

    @allure.title("div_{get_div_int_error_datas_with_fixture[0]}_{get_div_int_error_datas_with_fixture[1]}")
    @allure.story("div Integer error Function")
    def test_div_int_zero(self, get_instance, get_div_int_error_datas_with_fixture):
        div_int_zero = get_div_int_error_datas_with_fixture
        with pytest.raises(ZeroDivisionError):  # pytest inner function
            get_instance.div(div_int_zero[0], div_int_zero[1])

    # @allure.title("相加")
    # @allure.story("相加功能")
    # @pytest.mark.run(order=4)
    # @pytest.mark.parametrize('a,b,expect', get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
    # def test_add(self, a, b, expect):
    #
    #     result = self.calc.add(a, b)
    #     assert expect == result
    #
    # @allure.story("相减功能")
    # @pytest.mark.run(order=3)
    # @pytest.mark.parametrize('a,b,expect', get_datas()['subtract']['datas'], ids=get_datas()['subtract']['ids'])
    # def test_subtract(self, a, b, expect):
    #     result = self.calc.subtract(a, b)
    #     assert expect == result
    #
    # @allure.story("相乘功能")
    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize('a,b,expect', get_datas()['multiply']['datas'], ids=get_datas()['multiply']['ids'])
    # def test_multiply(self, a, b, expect):
    #     result = self.calc.multiply(a, b)
    #     assert expect == result
    #
    # @allure.title("相除")
    # @allure.story("相除功能")
    # @pytest.mark.run(order=pythoncode)
    # @pytest.mark.parametrize('a,b,expect', get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
    # def test_div(self, a, b, expect):
    #     if b == 0:
    #         try:
    #             self.calc.div(a, b)
    #         except ZeroDivisionError as e:
    #             print("除数不能为0")
    #     else:
    #         result = self.calc.div(a, b)
    #         assert result == expect


if __name__ == '__main__':
    pytest.main(["-vs", "test_Calculator.py"])
