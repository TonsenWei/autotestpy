# -*- coding: utf-8 -*-
import pytest
import time
import allure
import os
import sys
import logging

sys.path.insert(0, '../')
from src.utils.log_util import LogUtil

project_path = os.path.dirname(os.path.abspath(__file__))
LogUtil().LOGGER.info("test_demo.py project_path = " + project_path)
workspace_path = os.path.dirname(project_path)
LogUtil().LOGGER.info("test_demo.py workspace_path = " + workspace_path)

# py文件内起作用，在该py文件所有测试类之前执行
def setup_module(module):
    LogUtil().LOGGER.debug("setup_module ...")

# py文件内起作用，在该py文件所有测试类之后执行
def teardown_module(module):
    LogUtil().LOGGER.debug("teardown_module ...")

# @pytest.mark.run(order=0)  # 执行的顺序
# @pytest.mark.last  # 最后一个执行，执行时可能会报警告PytestUnknownMarkWarning: Unknown pytest.mark.last，忽略
# @pytest.mark.skip(reason="debug ok")  # 是否忽略（不执行该py文件内的测试），模块级别
class TestDemo(object):

    # 类内所有测试用例执行之前执行
    def setup_class(self):
        LogUtil().LOGGER.debug("setup_class ...")
    
    # 类内所有测试用例执行之后执行
    def teardown_class(self):
        LogUtil().LOGGER.debug("teardown_class ...")
    
    # 测试用例
    @allure.feature("TestDemo")  # allure feature属性
    @allure.story("TestDemo")  # allure story属性
    # @pytest.mark.skip(reason="debug ok")  # 是否忽略，函数级别，不执行该条用例
    def test_case_001(self):
        '''
        this is a test demo docstring
        '''
        with allure.step("step 1: sum"):
            sum = 1 + 2
        with allure.step("step 2: mul"):
            sum = sum * 2
        assert sum is 6
