import sys

import pytest

from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask
from task.SuiteTask import SuiteTask

browser_data = [{'browser_type': 'chrome', 'if_head': True}]


class TestSuites:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_test_suite(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        suite = SuiteTask(driver, data, capture, logger, atas_api)
        suite.create_suite(True, True)
        driver.get_driver().quit()
