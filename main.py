import pytest
import os
import sys
import platform
import subprocess
import time

from src.utils.log_util import LogUtil

# project dir path
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class Run:
    '''
    for use this class, install allure commandline tools first
    '''
    def __init__(self):
        super().__init__()
        self.project_path = os.path.dirname(os.path.abspath(__file__))
    
    def init_env(self):
        if os.path.exists(project_path + '/data'):
            # remove dir,  /s:remove folder and sub folders(not remove data dir), /q:silence mode,will not notice you
            if platform.system() is "Windows":
                cmd1 = 'rd /s/q ' + project_path + '\\data'
            else:
                cmd1 = 'rm -rf ' + project_path + '/data/*'
            LogUtil().LOGGER.debug(cmd1)
            subprocess.run(cmd1, shell=True)
        # copy dir or file, /D: copy new files only
        if platform.system() is "Windows":
            cmd2 = "xcopy /D/e " + project_path + "\\reports\\history " + project_path + "\\data\\history\\"
        else:
            cmd2 = "cp -a " + project_path + "/reports/history " + project_path + "/data"
        LogUtil().LOGGER.debug(cmd2)
        time.sleep(2)
        subprocess.run(cmd2, shell=True)
    
    def init_report(self):
        cmd1 = "allure generate " + self.project_path + "/data -o " + self.project_path + "/reports --clean"
        cmd2 = "allure open -h localhost -p 8099 " + self.project_path + "/reports"
        subprocess.run(cmd1, shell=True)
        project_path = os.path.abspath(os.path.dirname(__file__))
        report_path = project_path + "/reports/" + "index.html"
        LogUtil().LOGGER.debug("report address:{}".format(report_path))
        proc = subprocess.run(cmd2, shell=True)  # auto open report, use ctrl + C to exit

if __name__ == "__main__":
    run = Run()
    run.init_env()
    pytest.main(["-v", "-s", project_path + "/tests", "--alluredir=" + project_path + "/data"])
    run.init_report()
