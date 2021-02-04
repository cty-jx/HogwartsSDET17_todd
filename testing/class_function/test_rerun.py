#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def test_rerun():
    # assert pythoncode == pythoncode
    # assert pythoncode == 2
    # assert 2==3
    pytest.assume(1 == 4)
    pytest.assume(1 == 2)
    pytest.assume(1 == 1)
    pytest.assume(2 == 1)
