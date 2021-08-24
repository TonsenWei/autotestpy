# -*- coding: utf-8 -*-
import subprocess
import sys
import os

sys.path.insert(0, '../')
from src.utils.log_util import LogUtil
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class CmdUtil():
    
    @staticmethod
    def excute_cmd(cmd):
        '''
        excute system command
        :param cmd: command to be run in system
        :return: 
        '''
        LogUtil().LOGGER.info(cmd)
        obj = subprocess.Popen(cmd, \
            shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while obj.poll() is None:
            # line = obj.stdout.readline().decode("utf-8", "replace").strip()
            line = obj.stdout.readline().decode("utf-8", "replace")
            # if line.strip() is not "":
            LogUtil().LOGGER.info(line.strip())
        excute_cmd_result = obj.wait()
        LogUtil().LOGGER.debug("excute_cmd_result = " + str(excute_cmd_result))

    
    @staticmethod
    def excute_cmd_in_dir(cmd, cwd_dir = "./"):
        '''
        excute system command
        :param cmd: command to be run in system
        :param cwd_dir: directory to run command
        :return: 
        '''
        LogUtil().LOGGER.info(cmd + ", dir: " + cwd_dir)
        obj = subprocess.Popen(cmd, \
            shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd_dir)
        while obj.poll() is None:
            # line = obj.stdout.readline().decode("utf-8", "replace").strip()
            line = obj.stdout.readline().decode("utf-8", "replace")
            # if line.strip() is not "":
            LogUtil().LOGGER.info(line.strip())
        excute_cmd_result = obj.wait()
        LogUtil().LOGGER.debug("excute_cmd_in_dir = " + str(excute_cmd_result))

if __name__ == "__main__":
    CmdUtil.excute_cmd("dir")