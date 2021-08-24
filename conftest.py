# -*- coding: utf-8 -*-
import pytest
import base64
import allure

from src.utils.log_util import LogUtil

# 每个测试用例执行都会执行，且在setup、call、teardown阶段都会执行
@pytest.hookimpl(tryfirst=True, hookwrapper=True)  
def pytest_runtest_makereport(item, call):
    """
    每个测试用例执行后，制作测试报告
    :param item: 测试用例对象
    :param call: 测试用例的测试步骤
            执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
    :return:
    """
    # 获取常规钩子方法的调用结果,返回一个result对象 
    out = yield 
    # 获取调用结果的测试报告，返回一个report对象, report对象的属性包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、outcome(用例的执行结果，passed,failed)
    report = out.get_result()
    report.description = str(item.function.__doc__)  # 获取函数注释
    # if str(report.nodeid) == "tests/test_demo.py::TestDemo::test_case_001":
        # LogUtil().LOGGER.warning("out = " + str(out)) 
        # LogUtil().LOGGER.warning("report = " + str(report))
        # LogUtil().LOGGER.warning("report.nodeid = " + str(report.nodeid))
        # LogUtil().LOGGER.warning("report.outcome = " + str(report.outcome))
        # LogUtil().LOGGER.warning("report.when = " + str(report.when))
        # LogUtil().LOGGER.warning("report.failed = " + str(report.failed))
        # LogUtil().LOGGER.warning("report.description = " + str(report.description))
    if report.when == "call" and report.failed:  # 如果用例被调用且已失败
        '''
        使用场景：用例失败后截图，抓取打包日志等
        '''
        LogUtil().LOGGER.warning("call is call and test fail") 
        # 添加txt附件
        allure.attach.file('./py_log.txt', 'py_log', allure.attachment_type.TEXT)
        # allure.attach.file('./images/G6SA_FM_107_1_MHz.png', '区域截图', allure.attachment_type.PNG)
        # allure.attach.file('./images/g6sa.png', '全屏截图', allure.attachment_type.PNG)
        # LogUtil().LOGGER.warning("out = " + str(out)) 
        # LogUtil().LOGGER.warning("report = " + str(report))
        # LogUtil().LOGGER.warning("report.nodeid = " + str(report.nodeid))
        # LogUtil().LOGGER.warning("report.outcome = " + str(report.outcome))
        # LogUtil().LOGGER.warning("report.when = " + str(report.when))
        # LogUtil().LOGGER.warning("report.failed = " + str(report.failed))
        # LogUtil().LOGGER.warning("report.description = " + str(report.description))